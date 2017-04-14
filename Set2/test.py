import Challenge09
import unittest


class testSet2(unittest.TestCase):
    def setUp(self):
        pass

    def testChallenge09(self):
        expected = b'YELLOW SUBMARINE\x04\x04\x04\x04'
        self.assertEqual(Challenge09.main(), expected)


if __name__ == '__main__':
    unittest.main()
