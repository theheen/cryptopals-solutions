import sys
sys.path.insert(0, '../utility')
from utility import char_XOR, x2

def main():
    strings = []
    with open('4.txt') as f:
        for line in f:
            strings.append(bytes.fromhex(line[:60]))

    best = 0
    bestscore = 9999
    key = ''
    for count, line in enumerate(strings):
        mindist = 9999
        bestchar = ''
        for n in range(256):
            distance = x2(char_XOR(line, n))
            if distance < mindist:
                mindist = distance
                bestchar = n
        if mindist < bestscore:
            bestscore = mindist
            best = count
            key = bestchar
    return char_XOR(strings[best], key)

if __name__ == '__main__':
    print(main())
