import unittest
from gcd import gcd


class TestGcd(unittest.TestCase):
    def test_gcd(self):
        """
        最大公約数を求められるか
        """

        TestCase = tuple[str, tuple[int, int], int]  # TestCase型 (メッセージ, 引数, 期待値)
        testCases: tuple[TestCase, ...] = (
            ("12, 18の最大公約数は6である", (12, 18), 6),
            ("18, 12の最大公約数は6である", (18, 12), 6),
            ("13, 8の最大公約数は1である", (13, 8), 1),
            ("16, 8の最大公約数は8である", (16, 8), 8),
            ("45, 135の最大公約数は45である", (45, 135), 45),
            ("0, 135の最大公約数は0である", (0, 135), 135),
            ("135, 0の最大公約数は0である", (135, 0), 135),
            ("1350, 0の最大公約数は0である", (1350, 0), 1350),
        )

        for testCase in testCases:
            actual = gcd(*testCase[1])
            self.assertEqual(testCase[2], actual, testCase[0])


if __name__ == '__main__':
    unittest.main()
