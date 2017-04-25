from os import urandom
import collections
import base64
import sys
sys.path.insert(0, '../utility')
from utility import ecb_encrypt, split_into_blocks

key = urandom(16)


def ecb_encryptor(text):
    secret = b"""Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK"""
    dec = base64.b64decode(secret)
    ecb_input = b''.join([text, dec])
    blocks = split_into_blocks(ecb_input, 16)
    enc = ecb_encrypt(blocks, key)
    return b''.join(enc)


def detect_blocksize():
    test_input = b''
    initial_size = len(ecb_encryptor(test_input))
    size = initial_size
    while size == initial_size:
        test_input += b'x'
        size = len(ecb_encryptor(test_input))
    return size - initial_size


def hidden_message_length():
    initial = len(ecb_encryptor(b''))
    observed = initial
    pad_len = 0
    while observed == initial:
        padding = b''.join([b'A'] * pad_len)
        observed = len(ecb_encryptor(padding))
        pad_len += 1
    return initial - pad_len


def ecb_or_cbc(blocksize):
    text = b''.join([b'x'] * 160)
    enc = ecb_encryptor(text)
    countdict = collections.defaultdict(int)
    for n in range(0, len(enc), blocksize):
        block = enc[n:n + blocksize]
        countdict[block] += 1
    block_count = len(enc) // blocksize
    repeated_blocks = block_count - len(countdict)
    if repeated_blocks > 1:
        return "ECB"
    else:
        return "CBC"


def main():
    blocksize = detect_blocksize()
    if ecb_or_cbc(blocksize) != "ECB":
        raise ValueError("Expected to detect ECB")
    message_length = hidden_message_length()

    extracted = b''
    blockcount = 1
    while len(extracted) < message_length:
        for i in range(blocksize, 0, -1):
            input_padding = b''.join([b'A'] * (i - 1))
            blocks_length = blocksize * blockcount
            target = ecb_encryptor(input_padding)[:blocks_length]
            for b in range(256):
                byte = bytes([b])
                test_input = b''.join([input_padding, extracted, byte])
                test_output = ecb_encryptor(test_input)[:blocks_length]
                if test_output == target:
                    extracted = b''.join([extracted, byte])
                    break
            if len(extracted) >= message_length:
                break
        blockcount += 1

    return extracted


if __name__ == '__main__':
    print(main())
