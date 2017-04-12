def main():
    a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    b = bytes.fromhex("686974207468652062756c6c277320657965")

    out = []
    for x in range(len(a)):
        out.append(a[x] ^ b[x])

    xord = bytes(out).hex()
    return xord

if __name__ == '__main__':
    print(main())
