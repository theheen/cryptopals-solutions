from os import urandom
import random
import collections
import sys
sys.path.insert(0, '../utility')
from utility import cbc_encrypt, ecb_encrypt, split_into_blocks


def encryption_oracle(text, cheat=False):
    key = urandom(16)
    precount = random.randint(5, 10)
    pre = urandom(precount)
    postcount = random.randint(5, 10)
    post = urandom(postcount)
    randomsandwich = b''.join([pre, text, post])
    blocks = split_into_blocks(randomsandwich, 16)

    cointoss = random.randint(0, 1)
    if cointoss:
        IV = urandom(16)
        enc = cbc_encrypt(blocks, key, IV)
        enc = b''.join(enc)
    else:
        ecb_input = b''.join(blocks)
        enc = ecb_encrypt(ecb_input, key)

    if cheat:
        return (enc, cointoss)
    else:
        return enc


def main():
    text = b''.join([b'x'] * 160)
    enc, algo_choice = encryption_oracle(text, True)
    countdict = collections.defaultdict(int)
    for n in range(0, len(enc), 16):
        block = enc[n:n + 16]
        countdict[block] += 1
    block_count = len(enc) // 16
    repeated_blocks = block_count - len(countdict)
    if repeated_blocks > 1:
        if algo_choice == 0:  # CBC
            return (True, "CBC")
        else:
            return (False, "ECB")
    else:
        if algo_choice == 1:  # ECB
            return (True, "ECB")
        else:
            return (False, "CBC")


if __name__ == '__main__':
    success, alg = main()
    if success:
        print("Correctly identified", alg)
    else:
        print("Failed to identify", alg)
