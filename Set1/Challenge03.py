import sys
sys.path.insert(0, '../utility')
from utility import charXOR, x2


def main():
    x = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c7837"
                      "3e783a393b3736")
    xord = []
    for i in bytes(range(256)):
        score = x2(charXOR(x, i))
        xord.append((i, score))

    result = sorted(xord, key=lambda pair: pair[1])
    return charXOR(x, result[0][0])

if __name__ == '__main__':
    print(main())
