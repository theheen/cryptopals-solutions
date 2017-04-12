import string


def charXOR(textbytes, ch):
    out = []
    for x in range(len(textbytes)):
        out.append(textbytes[x] ^ ch)
    return bytes(out)


def repeatingXOR(textbytes, key):
    keysize = len(key)
    out = []
    for x in range(len(textbytes)):
        out.append(textbytes[x] ^ key[x % keysize])
    return bytes(out)


def x2(textbytes):
    score = 0
    length = len(textbytes)
    for i in string.ascii_lowercase:
        count = textbytes.count(ord(i))
        f = count / length
        expected = charprob.get(i)
        score += ((f - expected)**2) / expected
    return score


def hamming(x, y):
    if len(x) != len(y):
        raise ValueError("Undefined for sequences of unequal length")
    score = 0
    for i in range(len(x)):
        score += bin(x[i] ^ y[i]).count('1')
    return score


charprob = {
    'e': 12.702,
    't': 9.056,
    'a': 8.167,
    'o': 7.507,
    'i': 6.966,
    'n': 6.749,
    's': 6.327,
    'h': 6.094,
    'r': 5.987,
    'd': 4.253,
    'l': 4.025,
    'c': 2.782,
    'u': 2.758,
    'm': 2.406,
    'w': 2.360,
    'f': 2.228,
    'g': 2.015,
    'y': 1.974,
    'p': 1.929,
    'b': 1.492,
    'v': 0.978,
    'k': 0.772,
    'j': 0.153,
    'x': 0.150,
    'q': 0.095,
    'z': 0.074
}
