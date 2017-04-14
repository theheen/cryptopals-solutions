import sys
sys.path.insert(0, '../utility')
from utility import pad_single_block


def main():
    unpadded = b"YELLOW SUBMARINE"
    padded = pad_single_block(unpadded, 20)
    return padded


if __name__ == '__main__':
    print(main())
