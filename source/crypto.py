from secrets import token_bytes
from typing import Tuple

def getKey(lenght: int) -> int:
    tb: bytes = token_bytes(lenght)
    return int.from_bytes(tb, 'big')
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes : bytes = original.encode()
    dummy : int = getKey(len(original_bytes))
    original_key : int = int.from_bytes(original_bytes, 'big')
    encrypted : int = original_key ^ dummy
    return dummy, encrypted
def decrypt(key_1: int, key_2: int) -> str:
    decrypted : int = key_1 ^ key_2
    temp : bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return temp.decode()

key_1, key_2 = encrypt('secredo')
print(key_1, key_2)
result: str = decrypt(key_1, key_2)
print(result)