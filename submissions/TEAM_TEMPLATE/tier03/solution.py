"""Tier 3 solution for your team.

The checker runs this file from the repo root. Keep these imports; they work
there, while the notebook's `import helper` does not.
"""
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

from common import load_locked, keystream, xor_bytes
from tier03 import helper


def build_circuit():
    """Return your main circuit. Used for diagrams only, never for scoring."""
    raise NotImplementedError


def solve():
    """Run your circuit on Aer and return the decrypted line as a string."""
    raise NotImplementedError
