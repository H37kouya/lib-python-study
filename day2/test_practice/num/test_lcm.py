import unittest
from lcm import lcm


class TestLcm(unittest.TestCase):
    def test_lcm(self):
        """
        最小公倍数を求められるか
        """

        TestCase = tuple[str, tuple[int, int], int]  # TestCase型 (メッセージ, 引数, 期待値)
        testCases: tuple[TestCase, ...] = (
            ("12, 18の最小公倍数は36である", (12, 18), 36),
            ("18, 12の最小公倍数は36である", (18, 12), 36),
            ("13, 8の最小公倍数は13*8である", (13, 8), 13 * 8),
            ("16, 8の最小公倍数は16である", (16, 8), 16),
            ("45, 135の最小公倍数は135である", (45, 135), 135),
            ("0, 135の最小公倍数は0である", (0, 135), 0),
            ("135, 0の最小公倍数は0である", (135, 0), 0),
        )

        for testCase in testCases:
            actual = lcm(*testCase[1])
            self.assertEqual(testCase[2], actual, testCase[0])


if __name__ == '__main__':
    unittest.main()
