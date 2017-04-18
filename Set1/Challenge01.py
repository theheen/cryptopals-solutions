import base64


def main():
    x = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    by = bytes.fromhex(x)
    b64 = base64.b64encode(by)
    return b64


if __name__ == "__main__":
    print(main())
