import collections


def main():
    strings = []

    with open('8.txt') as f:
        for line in f:
            strings.append(bytes.fromhex(line[:320]))

    scores = {}
    for s in strings:
        count = collections.defaultdict(int)
        for n in range(0, len(s), 16):
            block = s[n:n + 16]
            count[block] += 1
        scores[s] = 20 - len(count)

    results = sorted(scores, key=lambda x: scores[x], reverse=True)
    return results[0].hex()


if __name__ == '__main__':
    print("String", main(), "is probably encrypted by AES in ECB mode.")
