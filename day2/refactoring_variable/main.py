def main_before(a: int, b: int) -> None:
    c = 1
    s = 0
    for i in range(a, b, c):
        if i % 2 == 0:
            s += i

    print(s)


if __name__ == '__main__':
    main_before(10, 99)
