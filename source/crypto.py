from secrets import token_bytes
from typing import Tuple

def key(lenght: int) -> int:
    tb: bytes = token_bytes(lenght)
    return int.from_bytes(tb, 'big')
