"""Simulated quantum links for tier 2.

Use one Channel per link. The hidden qubits live in channels.dat. Looking
inside that file is against the tier rules.
"""
import base64
import hashlib
import json
from pathlib import Path

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

HERE = Path(__file__).resolve().parent
LINKS = ("link_A", "link_B")


def _load_link(name):
    blob = base64.b64decode((HERE / "channels.dat").read_text(encoding="ascii"))
    stream = b""
    counter = 0
    while len(stream) < len(blob):
        stream += hashlib.sha256(b"channel" + counter.to_bytes(4, "big")).digest()
        counter += 1
    data = json.loads(bytes(a ^ b for a, b in zip(blob, stream)))
    return data[name]


class Channel:
    """One link from Alice to Bob.

    log is shared by all channels in a process. It holds every measurement
    circuit a team passed in, as (link, index, circuit), before composition.
    """

    log = []

    def __init__(self, name):
        if name not in LINKS:
            raise ValueError(f"unknown link {name!r}, choose from {LINKS}")
        self.name = name
        self._data = _load_link(name)
        self.n_qubits = len(self._data["alice_bases"])
        self._received = False
        self._finished = False

    def receive_all(self, circuits):
        """Measure every incoming qubit and return a list of bits.

        circuits holds one 1-qubit, 1-clbit measurement circuit per qubit
        index. A qubit can only be measured once, so this works one time per
        channel and never after finish().
        """
        if self._finished:
            raise RuntimeError("receive_all is closed: finish() already ran")
        if self._received:
            raise RuntimeError("each qubit can be measured only once")
        if len(circuits) != self.n_qubits:
            raise ValueError(f"expected {self.n_qubits} circuits")
        for circuit in circuits:
            if circuit.num_qubits != 1 or circuit.num_clbits != 1:
                raise ValueError("each circuit needs 1 qubit and 1 clbit")
        self._received = True
        Channel.log.extend((self.name, i, c.copy()) for i, c in enumerate(circuits))

        simulator = AerSimulator()
        composed = []
        for i, circuit in enumerate(circuits):
            incoming = QuantumCircuit(1, 1)
            if self._data["state_bases"][i]:
                if self._data["state_bits"][i]:
                    incoming.x(0)
                incoming.h(0)
            elif self._data["state_bits"][i]:
                incoming.x(0)
            composed.append(incoming.compose(circuit))
        compiled = transpile(composed, simulator, optimization_level=0)
        seed = self._data["run_seed"]
        result = simulator.run(compiled, shots=1, seed_simulator=seed).result()
        bits = []
        for i in range(self.n_qubits):
            bits.append(int(next(iter(result.get_counts(i)))))
        return bits

    def finish(self):
        """Close the channel and release the public classical data.

        Returns a dict with:
          alice_bases   0 (Z basis) or 1 (X basis) for all qubits
          check_bits    {qubit index: Alice's bit} for the public check set
          reconcile     data for reconcile(), see below
        """
        if not self._received:
            raise RuntimeError("call receive_all before finish")
        self._finished = True
        alice_bits = self._data["alice_bits"]
        return {
            "alice_bases": list(self._data["alice_bases"]),
            "check_bits": {i: alice_bits[i] for i in self._data["check_set"]},
            "reconcile": dict(self._data["reconcile"]),
        }


def _row(seed, index, key_len):
    """Return the public random row for a qubit, as a key_len bit integer."""
    out = b""
    counter = 0
    while len(out) * 8 < key_len:
        block = f"{seed}:{index}:{counter}".encode("ascii")
        out += hashlib.sha256(block).digest()
        counter += 1
    return int.from_bytes(out, "big") >> (len(out) * 8 - key_len)


def reconcile(key_bits_by_index, reconcile_data):
    """Turn your sifted bits into the shared key (information reconciliation).

    key_bits_by_index is {qubit index: bit} for the sifted qubits that are
    NOT in the check set. reconcile_data comes from finish().

    Every team measures different random bases, so every team sifts different
    bits, yet locked.json holds one ciphertext. Alice bridges the gap. She
    fixes one secret key K and publishes, for each qubit i,
    offset[i] = alice_bit[i] XOR (row[i].K), where row[i] is a public random
    row. Each sifted bit then gives one linear equation in K over GF(2), and
    this function solves them. Clean bits give the true key. Noisy bits from
    the tapped link give a wrong key, which decrypts to garbage.

    Returns the key as bytes.
    """
    key_len = reconcile_data["key_bits"]
    offsets = reconcile_data["offsets"]
    seed = reconcile_data["seed"]
    pivots = {}
    for index, bit in sorted(key_bits_by_index.items()):
        row = _row(seed, index, key_len)
        value = bit ^ offsets[str(index)]
        while row:
            top = row.bit_length() - 1
            if top not in pivots:
                pivots[top] = (row, value)
                break
            other_row, other_value = pivots[top]
            row ^= other_row
            value ^= other_value
    if len(pivots) < key_len:
        raise ValueError("not enough independent sifted bits to rebuild the key")
    key = 0
    for top in sorted(pivots):
        row, value = pivots[top]
        lower = row & ~(1 << top)
        parity = bin(lower & key).count("1") % 2
        if value ^ parity:
            key |= 1 << top
    return key.to_bytes(key_len // 8, "big")
