import sys
sys.path.insert(0, '../utility')
from utility import padSingleBlock


def main():
    unpadded = b"YELLOW SUBMARINE"
    padded = padSingleBlock(unpadded, 20)
    return padded


if __name__ == '__main__':
    print(main())
