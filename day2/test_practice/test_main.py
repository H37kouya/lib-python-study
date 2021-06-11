import unittest
from main import add


class TestMain(unittest.TestCase):
    """
    Test class of main.py
    """

    def test_add(self):
        """
        足し算が正しくできるか
        """
        arg1 = 4
        arg2 = 3
        expected = 7
        self.assertEqual(expected, add(arg1, arg2))

    def test_add_assertion_roulette(self):
        """
        足し算が正しくできるか (アサーションルーレット)
        """

        TestCase = tuple[str, tuple[int, int], int]  # TestCase型 (メッセージ, 引数, 期待値)
        testCases: tuple[TestCase, ...] = (
            ("4+3は7である", (4, 3), 7),
            ("11+10は7である", (11, 10), 21),
            ("-1-1は-2である", (-1, -1), -2),
            ("0+0は0である", (0, 0), 0),
        )

        for testCase in testCases:
            actual = add(*testCase[1])
            self.assertEqual(testCase[2], actual, testCase[0])

if __name__ == '__main__':
    unittest.main()