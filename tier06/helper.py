"""Helpers for tier 6: the same toy cipher, 14-bit key. No oracle is provided."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common.toy_cipher import (  # noqa: E402,F401
    PERM,
    ROUND_CONSTANT,
    SBOX,
    SBOX_GATES,
    ToyCipher,
    mask_gates,
)

KEY_BITS = 14


def checksum(data):
    """Return the public checksum of a byte string: sum of bytes mod 256."""
    return sum(data) % 256
