"""Helpers for tier 5: the published toy cipher. No oracle is provided."""
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

KEY_BITS = 10
