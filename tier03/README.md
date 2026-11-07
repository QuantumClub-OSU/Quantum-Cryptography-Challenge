# Tier 3: Twenty-Four Seals

**Level:** Easy. **Points:** see [SCORING.md](../SCORING.md).

Twenty-four sealed oracles each hide one key bit. Each one is promised to be either constant (the same output for every input) or balanced (output 1 on exactly half the inputs). You may ask each one a single question.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: SHA-256 keystream XOR, 24-bit key.

Oracle i gives key bit i: 0 for constant, 1 for balanced. `key_bits` is the 24 bits as a string, oracle 0 first. Ciphertext = plaintext XOR `keystream(key_bits, length)`.

The decrypted line starts with `QC-03: `.

## What is provided

- `locked.json`: oracle count, input size, and the ciphertext.
- `oracle_00.qpy` to `oracle_23.qpy`: one oracle each, on 6 input qubits plus a target.
- `helper.build_oracle(i)`: loads oracle i as a 7-qubit circuit. Qubits 0 to 5 hold x and qubit 6 is the target.
- `helper.count_oracle_calls(circuit)`: counts oracle applications.

## What is NOT provided

Which oracles are constant and which are balanced.

## Rules for this tier

- Each oracle may be applied once. Run one circuit per oracle, with one oracle application each.
- Do not classify oracles by inspecting their gates or by simulating their matrices.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

Asked about one input at a time, a single question cannot tell the two kinds apart. A question about all 64 inputs at once can.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

Turn each output into a sign. A constant oracle puts the same sign on every input, and a balanced one puts + on half and - on the other half. Undo the superposition and ask how often you land back on all zeros.

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
