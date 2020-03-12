
from _md5 import md5

from app.commons.utils.constants import Base62


def to_base_62(num):
    alphabet = Base62.ALPHABETS
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def string_encode(string):
    md5_hash = md5(string.encode('utf-8')).hexdigest()
    size = len(md5_hash)
    x = md5_hash[:size//3]
    y = md5_hash[size//3:-size//3]
    z = md5_hash[-size//3:]
    x_as_int = int(x, 16)
    y_as_int = int(y, 16)
    z_as_int = int(z, 16)
    xor = x_as_int ^ y_as_int ^ z_as_int
    hash_val = to_base_62(xor)
    return hash_val
