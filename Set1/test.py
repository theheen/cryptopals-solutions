import Challenge01
import Challenge02
import Challenge03
import Challenge04
import Challenge05
import Challenge06
import Challenge07
import Challenge08
import unittest


class testSet1(unittest.TestCase):
    def setUp(self):
        pass

    def testChallenge01(self):
        expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(Challenge01.main(), expected)

    def testChallenge02(self):
        expected = "746865206b696420646f6e277420706c6179"
        self.assertEqual(Challenge02.main(), expected)

    def testChallenge03(self):
        expected = b"Cooking MC's like a pound of bacon"
        self.assertEqual(Challenge03.main(), expected)

    def testChallenge04(self):
        expected = b'Now that the party is jumping\n'
        self.assertEqual(Challenge04.main(), expected)

    def testChallenge05(self):
        expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
        self.assertEqual(Challenge05.main(), expected)

    def testChallenge06(self):
        with open('06-out.txt') as f:
            expected = f.read()
        self.assertEqual(Challenge06.main(), expected)

    def testChallenge07(self):
        with open('07-out.txt', 'rb') as f:
            expected = f.read()
        self.assertEqual(Challenge07.main(), expected)

    def testChallenge08(self):
        expected = "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a"
        self.assertEqual(Challenge08.main(), expected)


if __name__ == '__main__':
    unittest.main()
