from gcd import gcd


def lcm(x: int, m: int) -> int:
    if x == 0 or m == 0:
        return 0

    return int(x * m / gcd(x, m))
