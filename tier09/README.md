# Tier 9: The Wrapped Key, N = 77

**Level:** Very hard. **Points:** see [SCORING.md](../SCORING.md).

The same scheme with N = 77. There is no shortcut for special moduli here, so modular multiplication needs real construction work.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: RSA-wrapped key, SHA-256 keystream XOR.

Same as tier 8: derive d, compute k = c^d mod N, then `key_bits = format(k, f"0{key_width_bits}b")`. Ciphertext = plaintext XOR `keystream(key_bits, length)`.

The decrypted line starts with `QC-09: `.

## What is provided

- `locked.json`: N, public exponent e, `wrapped_key` c = k^e mod N, `key_width_bits`, and the ciphertext.

## What is NOT provided

Any helper. You have only public parameters.

## Rules for this tier

- Factor N with the help of a quantum circuit, as in tier 8.
- Building modular multiplication as a permutation-based unitary is allowed at these sizes, but you must explain your construction.
- Dense `UnitaryGate` constructions can transpile very slowly. If transpiling passes `transpile_timeout_s`, you keep your tier points but earn no simplicity points for this tier.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

Everything from tier 8 carries over. The hard part is a controlled multiplication by a mod 77 on 7 work qubits.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

Multiplying by a number coprime to 77 only reorders 0 to 76. A reordering can be built as a circuit, or as a permutation matrix to get started.

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
