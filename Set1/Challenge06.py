import sys
sys.path.insert(0, '../utility')
import base64
from utility import hamming, charXOR, x2


def main():
    text = ""
    with open('6.txt') as f:
        text = f.read()
    decoded = base64.b64decode(text)

    distance = 99999
    key = 0
    keyresult = []
    for keysize in range(2, 50):
        x = 0
        for i in range(10):
            x += hamming(decoded[i * keysize:(i + 1) * keysize],
                         decoded[(i + 1) * keysize:(i + 2) * keysize])
        x /= (10 * keysize)
        keyresult.append((keysize, x))
        if x < distance:
            distance = x
            key = keysize
    goodkeys = sorted(keyresult, key=lambda x: x[1])
    key = goodkeys[0][0]

    # Assuming key is correct:
    #   split input into blocks, mod keysize
    #   decode blocks using x2
    #   recombine decoded blocks

    # Split
    blocks = [[] for __ in range(key)]
    for i in range(len(decoded)):
        blocks[i % key].append(decoded[i])

    # Decode
    keystring = ""
    for x in range(key):
        xord = []
        for i in bytes(range(256)):
            score = x2(charXOR(blocks[x], i))
            xord.append((i, score))
        result = sorted(xord, key=lambda pair: pair[1])
        keystring += chr(result[0][0])
        blocks[x] = charXOR(blocks[x], result[0][0])

    # print("KEY: ", keystring, "\n")

    # Recombine
    output = []
    for i in range(len(blocks[0])):
        for x in blocks:
            if i < len(x):
                output.append(x[i])

    return bytes.decode(bytes(output))


if __name__ == '__main__':
    print(main())
