"""Helpers for tier 4."""
from pathlib import Path

from qiskit import qpy

HERE = Path(__file__).resolve().parent


def build_oracle():
    """Return the oracle as a 20-qubit circuit.

    Qubits 0..9 hold x. Qubits 10..19 receive f(x) and MUST start in |0>. The
    oracle computes |x>|0> to |x>|f(x)>, and it is not meant for other
    starting values of the output register. Run
    `transpile(circuit, simulator)` before `simulator.run`.
    """
    with open(HERE / "oracle.qpy", "rb") as handle:
        return qpy.load(handle)[0]
