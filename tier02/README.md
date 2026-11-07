# Tier 2: Two Links

**Level:** Easy. **Points:** see [SCORING.md](../SCORING.md).

Alice sent Bob 1024 qubits on each of two links, each qubit prepared in a random basis. Eve sits on one of the links, measuring every qubit in a random basis and resending it. Play Bob: find the clean link and use it to rebuild the key.

Working out which quantum method opens this file is part of the tier. The hints at the end are optional.

## How the file is locked

`locked.json` labels it as: XOR with the reconciled key of the clean link.

Bases are 0 for Z and 1 for X. The key is `helper.reconcile` applied to `{index: bit}` for the right set of your measured bits, from the right link. Ciphertext = plaintext XOR key. Use `xor_bytes`.

Why reconcile? Every team picks different random bases, so every team keeps different bits, but `locked.json` has one ciphertext. Alice publishes one offset per qubit that ties your bits to her fixed key, and `reconcile` solves the resulting linear equations. Bits from the tapped link give a wrong key, which decrypts to garbage.

The decrypted line starts with `QC-02: `.

## What is provided

- `locked.json`: `n_qubits`, link names, and the ciphertext.
- `helper.Channel(name)`: one link, either `link_A` or `link_B`.
- `Channel.receive_all(circuits)`: takes one 1-qubit, 1-clbit measurement circuit per qubit index, composes each with the hidden incoming state, runs on Aer, and returns the bits.
- `Channel.finish()`: only after `receive_all`. Returns Alice's bases for all 1024 qubits, the bit values of the public check set (about 25% of the qubits), and the reconciliation data.
- `helper.reconcile(key_bits_by_index, reconcile_data)`: turns your chosen bits into the key.
- `channels.dat`: the hidden qubits, read only by `Channel`.

## What is NOT provided

Alice's bases before `finish()`, and which link is tapped.

## Rules for this tier

- Choose your bases blind, before `finish()`. After `finish()`, `receive_all` raises an error.
- Each qubit index can be measured once. This stands in for no-cloning. Do not make a second `Channel` for a link to measure it again, because the checker flags repeat measurements.
- Do not open `channels.dat` or read `Channel`'s private fields. The hiding here is by rule, not by cryptography.
- In a notebook, rerun from a fresh kernel or a fresh `Channel` only while developing. Your final `solve()` must measure each link once.
- A quantum circuit must run on Aer during `solve()` for full credit. See [CHALLENGE.md](../CHALLENGE.md).

## Hints

Open these only if you are stuck. They cost no points.

<details>
<summary>Hint 1: a nudge</summary>

A bit you measured is only worth keeping if you happened to measure it in the basis Alice prepared it in. `finish()` tells you her bases afterward.

</details>

<details>
<summary>Hint 2: a bigger nudge</summary>

Someone who measures in a random basis and resends disturbs some of the qubits you keep. Compare your kept bits with the check set Alice reveals: one link agrees almost perfectly and the other does not. Leave the check-set bits out of the key, since they are public.

</details>

## Presentation checklist

1. What the file hid, and how you worked out which quantum approach fits.
2. Why that approach works.
3. Circuit diagram with qubit and gate counts.
4. Measurement result and key extraction.
5. Classical cost for comparison.
