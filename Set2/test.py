import Challenge09
import Challenge10
import Challenge11
import Challenge12
import unittest


class testSet2(unittest.TestCase):
    def setUp(self):
        pass

    def testChallenge09(self):
        expected = b'YELLOW SUBMARINE\x04\x04\x04\x04'
        self.assertEqual(Challenge09.main(), expected)

    def testChallenge10(self):
        with open('10-out.txt', 'rb') as f:
            expected = f.read()
        self.assertEqual(Challenge10.main(), expected)

    def testChallenge11(self):
        self.assertIs(Challenge11.main()[0], True)

    def testChallenge12(self):
        with open('12-out.txt', 'rb') as f:
            expected = f.read()
        self.assertEqual(Challenge12.main(), expected)


if __name__ == '__main__':
    unittest.main()
