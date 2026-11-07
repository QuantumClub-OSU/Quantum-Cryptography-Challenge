"""Helpers for tier 3."""
from pathlib import Path

from qiskit import qpy

HERE = Path(__file__).resolve().parent
ORACLE_NAME = "tier3_oracle"


def build_oracle(i):
    """Return oracle i (0 to 23) as a 7-qubit circuit.

    Qubits 0..5 hold x and qubit 6 is the target. Run
    `transpile(circuit, simulator)` before `simulator.run`.
    """
    with open(HERE / f"oracle_{i:02d}.qpy", "rb") as handle:
        return qpy.load(handle)[0]


def count_oracle_calls(circuit):
    """Count oracle applications in a circuit, before transpiling it."""
    total = 0
    for instruction in circuit.data:
        operation = instruction.operation
        if operation.name == ORACLE_NAME:
            total += 1
        elif operation.definition is not None:
            total += count_oracle_calls(operation.definition)
    return total
