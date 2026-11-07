# Tier 6: The Bigger Safe

**Level:** Medium to hard. **Points:** see [SCORING.md](../SCORING.md).

The same cipher with a 14-bit key, and this time you only trust the first byte. About 64 keys pass that test, so your search has many answers and you must filter them.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: toy byte cipher, 14-bit key.

Same as tier 5, with a 14-bit key. The checksum is the sum of all plaintext bytes mod 256. Exactly one key passes it.

The decrypted line starts with `QC-06: `.

## What is provided

- `locked.json`: `key_bits`, the known prefix `Q`, a public `checksum`, and the ciphertext.
- `common/toy_cipher.py`, also through `helper.py`: the same cipher, plus `helper.checksum(data)`.

## What is NOT provided

The oracle, the number of passing keys, and how that number changes your circuit.

## Rules for this tier

- Treat only the first byte `Q` as known when building your oracle, even though the line format tells you more.
- Your circuit must account for many keys passing the test. Explain how that changed your circuit.
- Filter the measured candidates by decrypting the whole message and comparing the checksum.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

Your tier 5 oracle carries over, widened to 14 key bits.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

With M marked keys among N, the right number of repeats shrinks to about (pi/4) sqrt(N/M). You only know M roughly. What happens if your guess is a little high or low?

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
