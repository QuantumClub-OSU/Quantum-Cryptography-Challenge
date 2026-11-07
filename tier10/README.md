# Tier 10: The Handshake

**Level:** Boss. **Points:** see [SCORING.md](../SCORING.md).

Alice and Bob agreed on a secret by Diffie-Hellman in a small group. Recover one secret exponent with a quantum circuit and rebuild the shared secret.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: Diffie-Hellman shared secret, SHA-256 keystream XOR.

The shared secret is B^a mod p, where A = g^a mod p. `key_bits = format(secret, f"0{key_width_bits}b")`. Ciphertext = plaintext XOR `keystream(key_bits, length)`.

The decrypted line starts with `QC-10: `.

## What is provided

- `locked.json`: prime p, generator g, the order of g, public values A = g^a mod p and B = g^b mod p, `key_width_bits`, and the ciphertext.

## What is NOT provided

Any helper. You have only public parameters.

## Rules for this tier

- Recover one exponent with a quantum circuit. Do not find it classically, by brute force, or with a lookup table.
- Building modular multiplication as a permutation-based unitary is allowed at these sizes, but you must explain your construction.
- Dense `UnitaryGate` constructions can transpile very slowly. If transpiling passes `transpile_timeout_s`, you keep your tier points but earn no simplicity points for this tier.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

The order of g is public, and every power of g repeats with that period.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

Look at f(x1, x2) = g^x1 A^x2 mod p. It returns to 1 exactly when x1 + a x2 = 0 mod the order, so its repeating pattern in two dimensions hides a. Tier 8 measures a repetition in one dimension. Can you do two at once?

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
