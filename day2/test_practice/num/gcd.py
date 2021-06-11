def gcd(x: int, m: int) -> int:
    """
    最大公約数を求める

    ユークリッドの互除法
    """
    if m == 0:
        return x

    return gcd(m, x % m)
