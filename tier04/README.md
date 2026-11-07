# Tier 4: The Echo

**Level:** Medium. **Points:** see [SCORING.md](../SCORING.md).

A function on 10 bits repeats under XOR with a hidden nonzero string s: f(x) = f(x XOR s), and it is exactly 2-to-1. Finding s classically takes about 2^(n/2) queries. A quantum circuit needs about n runs.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: SHA-256 keystream XOR, 10-bit key.

Bit j of s is the value on qubit j. `key_bits = format(s, "010b")`. Ciphertext = plaintext XOR `keystream(key_bits, length)`.

The decrypted line starts with `QC-04: `.

## What is provided

- `locked.json`: `n` and the ciphertext.
- `oracle.qpy`: the oracle on 10 + 10 qubits.
- `helper.build_oracle()`: loads it. Qubits 0 to 9 hold x. Qubits 10 to 19 receive f(x) and must start in |0>.

## What is NOT provided

A GF(2) solver. Writing the classical step is part of the tier.

## Rules for this tier

- Recover s from the measurement results of circuits that apply the oracle.
- Do not recover s by reading the oracle's gates.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

Query every x at once, then measure the output register. The input register is left in an equal mix of some x and x XOR s.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

Hadamards on the input register after the oracle turn each run into one linear equation about s, mod 2. How many independent equations pin down a nonzero s?

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
