from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64


def main():
    backend = default_backend()
    key = b'YELLOW SUBMARINE'
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)

    text = b''
    with open('7.txt', "r") as f:
        text = f.read()

    text = base64.b64decode(text)

    decryptor = cipher.decryptor()
    out = decryptor.update(text)
    return out

if __name__ == '__main__':
    # print(main())
    with open('07-out.txt', 'wb') as f:
        f.write(main())
