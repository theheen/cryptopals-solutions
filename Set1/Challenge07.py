import sys
sys.path.insert(0, '../utility')
from utility import ecb_decrypt
import base64


def main():
    key = b'YELLOW SUBMARINE'
    with open('7.txt', "r") as f:
        text = f.read()
    text = base64.b64decode(text)
    out = ecb_decrypt(text, key)
    return out


if __name__ == '__main__':
    print(main())
