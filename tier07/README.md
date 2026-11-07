# Tier 7: The Hidden Angle

**Level:** Hard. **Points:** see [SCORING.md](../SCORING.md).

A one-qubit gate U carries a secret angle. Its eigenvalues are 1 and e^(2 pi i phi), and phi is the 14-bit key divided by 2^14.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: SHA-256 keystream XOR, 14-bit key.

With k the 14-bit integer and phi = k / 2^14, `key_bits = format(k, "014b")`. Ciphertext = plaintext XOR `keystream(key_bits, length)`.

The decrypted line starts with `QC-07: `.

## What is provided

- `locked.json`: `key_bits` and the ciphertext.
- `unitary.qpy`: U = V diag(1, e^(2 pi i phi)) V-dagger, for a hidden V.
- `eigenstate.qpy`: prepares V|1>, the eigenstate with eigenvalue e^(2 pi i phi).
- `helper.build_unitary()` and `helper.build_eigenstate()`: load those circuits.

## What is NOT provided

Controlled versions of U, and whatever readout circuit you need.

## Rules for this tier

- Measure phi with a quantum circuit that uses U.
- Do not compute the eigenvalues of U classically and call it solved. A team may use the matrix of U to build a power of U as one gate, if it explains the step and still measures the phase.
- U's global phase matters once it is controlled.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

phi = k / 2^14 has an exact 14-bit binary expansion, so it can be read out exactly, one bit per qubit.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

On its eigenstate, a controlled U leaves the eigenstate alone and puts the phase on the control qubit instead. Applying U 2^j times multiplies that phase by 2^j. How do fourteen such phases on fourteen control qubits become fourteen bits?

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
