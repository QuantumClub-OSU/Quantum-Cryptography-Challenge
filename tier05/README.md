# Tier 5: The Small Safe

**Level:** Medium. **Points:** see [SCORING.md](../SCORING.md).

A toy byte cipher with a 10-bit key guards this file, and you know how the message starts. Trying all 1024 keys classically is easy at this size. Your job is to build the key check as a reversible circuit and let a quantum circuit find the key.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: toy byte cipher, 10-bit key.

The key is the integer k, where key bit j has value 2**j. Decrypting byte i is: XOR with `mask(k, i)`, apply the S-box to both nibbles, apply `PERM`. For the first byte, i = 0 and the mask is exactly what `mask_gates` writes. For byte i, rotate the key left by 3i bits first, which only relabels key wires, then XOR `ROUND_CONSTANT * i mod 256`. PERM needs no gates, because it only relabels wires.

Several keys always decrypt the first byte to `Q`, so one byte is not enough. The first two bytes, `QC`, pin down a single key, so your oracle must check both.

The decrypted line starts with `QC-05: `.

## What is provided

- `locked.json`: `key_bits`, the known prefix `QC-05:`, and the ciphertext.
- `common/toy_cipher.py`, also through `helper.py`: `ToyCipher` as a Python class, plus the gate-level description in `SBOX_GATES`, `PERM`, and `mask_gates(key_bits)`.

## What is NOT provided

The oracle. You build it.

## Rules for this tier

- Your circuit must contain a reversible oracle that you built, which marks the keys that decrypt the known text correctly. Running your circuit must make the right key the likely measurement.
- Measuring random keys and checking them classically does not count.
- Classical checking of measured keys is fine.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

Write the decryption of one byte as reversible gates acting on the key qubits, then compare the result with the known byte. `mask_gates` and `SBOX_GATES` already describe the pieces. You can reuse the same 8 scratch wires for both bytes if you record the first comparison on one extra qubit and undo everything else.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

Marking the right key with a minus sign changes no measurement probability on its own. Pair the mark with a reflection about the uniform superposition, and repeat the pair. The number of repeats matters: about (pi/4) sqrt(number of keys), and too many makes it worse.

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
