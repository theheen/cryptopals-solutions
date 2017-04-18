import base64
import sys
sys.path.insert(0, '../utility')
from utility import split_into_blocks, cbc_decrypt


def main():
    key = b"YELLOW SUBMARINE"
    IV = bytes([0] * 16)
    with open('10.txt', 'rb') as f:
        text = f.read()
    text = base64.b64decode(text)
    blocks = split_into_blocks(text, 16)
    decrypted = cbc_decrypt(blocks, key, IV)
    return b''.join(decrypted)


if __name__ == '__main__':
    print(main())
