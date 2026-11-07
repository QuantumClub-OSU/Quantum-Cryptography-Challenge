"""Helpers for tier 7."""
from pathlib import Path

from qiskit import qpy

HERE = Path(__file__).resolve().parent


def build_unitary():
    """Return the 1-qubit circuit for U. Its global phase matters."""
    with open(HERE / "unitary.qpy", "rb") as handle:
        return qpy.load(handle)[0]


def build_eigenstate():
    """Return the 1-qubit circuit that prepares V|1> from |0>."""
    with open(HERE / "eigenstate.qpy", "rb") as handle:
        return qpy.load(handle)[0]
