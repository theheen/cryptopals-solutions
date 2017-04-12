import sys
sys.path.insert(0, '../utility')
from utility import repeatingXOR


def main():
    x = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    rXORd = repeatingXOR(x, key).hex()
    return rXORd

if __name__ == '__main__':
    print(main())
