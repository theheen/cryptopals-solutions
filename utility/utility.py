import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def _aes_ecb_cipher(key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    return cipher


def ecb_encrypt(blocks, key):
    cipher = _aes_ecb_cipher(key)
    encryptor = cipher.encryptor()
    enc = [encryptor.update(i) for i in blocks]
    return enc


def ecb_decrypt(text, key):
    cipher = _aes_ecb_cipher(key)
    decryptor = cipher.decryptor()
    dec = decryptor.update(text)
    return dec


def cbc_encrypt(blocks, key, IV):
    cipher = _aes_ecb_cipher(key)
    encryptor = cipher.encryptor()
    out = []
    prev = IV
    for b in blocks:
        xord = repeating_XOR(b, prev)
        enc = encryptor.update(xord)
        out.append(enc)
        prev = enc
    return out


def cbc_decrypt(blocks, key, IV):
    cipher = _aes_ecb_cipher(key)
    decryptor = cipher.decryptor()
    out = []
    prev = IV
    for b in blocks:
        dec = decryptor.update(b)
        xord = repeating_XOR(dec, prev)
        out.append(xord)
        prev = b
    return out


def split_into_blocks(text, size):
    blocks = []
    while len(text) >= size:
        blocks.append(text[:size])
        text = text[size:]
    if len(text) > 0:
        padded = pad_single_block(text, size)
    else:
        padded = bytes([size] * size)
    blocks.append(padded)
    return blocks


def pad_single_block(block, size):
    if len(block) > size:
        raise ValueError("Block is larger than given size")
    padSize = size - len(block)
    padding = bytes([padSize] * padSize)
    paddedBlock = b''.join([block, padding])
    return paddedBlock


def is_valid_padding(blocks):
    last_no = blocks[-1][-1]
    return blocks[-1][-last_no:] == bytes([last_no] * last_no)


def strip_padding(blocks):
    if not is_valid_padding(blocks):
        raise ValueError("Invalid padding.")
    last_no = blocks[-1][-1]
    out = blocks[:-1]
    out.append(blocks[-1][:-last_no])
    if len(out[-1]) == 0:
        return out[:-1]
    else:
        return out


def char_XOR(textbytes, ch):
    out = [x ^ ch for x in textbytes]
    return bytes(out)


def repeating_XOR(textbytes, key):
    keysize = len(key)
    out = [textbytes[x] ^ key[x % keysize] for x in range(len(textbytes))]
    return bytes(out)


def x2(textbytes):
    score = 0
    length = len(textbytes)
    for i in string.ascii_lowercase:
        count = textbytes.count(ord(i))
        f = count / length
        expected = charprob.get(i)
        score += ((f - expected)**2) / expected
    return score


def hamming(x, y):
    if len(x) != len(y):
        raise ValueError("Undefined for sequences of unequal length")
    score = 0
    for i in range(len(x)):
        score += bin(x[i] ^ y[i]).count('1')
    return score


charprob = {
    'e': 12.702,
    't': 9.056,
    'a': 8.167,
    'o': 7.507,
    'i': 6.966,
    'n': 6.749,
    's': 6.327,
    'h': 6.094,
    'r': 5.987,
    'd': 4.253,
    'l': 4.025,
    'c': 2.782,
    'u': 2.758,
    'm': 2.406,
    'w': 2.360,
    'f': 2.228,
    'g': 2.015,
    'y': 1.974,
    'p': 1.929,
    'b': 1.492,
    'v': 0.978,
    'k': 0.772,
    'j': 0.153,
    'x': 0.150,
    'q': 0.095,
    'z': 0.074
}
