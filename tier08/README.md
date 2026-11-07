# Tier 8: The Wrapped Key, N = 35

**Level:** Hard. **Points:** see [SCORING.md](../SCORING.md).

Textbook RSA wraps a small symmetric key. Factor the modulus and unwrap it.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: RSA-wrapped key, SHA-256 keystream XOR.

After factoring, derive d and compute k = c^d mod N. `key_bits = format(k, f"0{key_width_bits}b")`. Ciphertext = plaintext XOR `keystream(key_bits, length)`.

The decrypted line starts with `QC-08: `.

## What is provided

- `locked.json`: N, public exponent e, `wrapped_key` c = k^e mod N, `key_width_bits`, and the ciphertext.

## What is NOT provided

Any helper. You have only public parameters.

## Rules for this tier

- Factor N with the help of a quantum circuit. Do not factor N classically, for example by trial division.
- Classical post-processing of your measurements is fine, as are gcd and deriving d.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

Pick a base a with gcd(a, N) = 1. If you knew the smallest r with a^r = 1 mod N, and r is even, then gcd(a^(r/2) - 1, N) and gcd(a^(r/2) + 1, N) usually give the factors.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

x -> a^x mod N repeats with period r, and a quantum circuit can measure how often something repeats. The readout idea from tier 7 is a good place to start.

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
