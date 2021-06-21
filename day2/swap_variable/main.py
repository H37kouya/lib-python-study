def main() -> None:
    x = 1
    y = 1

    # before the
    tmp = x
    x = y
    y = tmp

    # after
    x, y = y, x
    print(x, y)


if __name__ == '__main__':
    main()
