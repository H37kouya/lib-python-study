from comp import Comp


def main() -> None:
    cp1 = Comp(3.0, 3.0)
    cp2 = Comp(2.0, 4.0)

    print("cp1の絶対値：", cp1.abs())
    print("cp1の複素共役：", cp1.conjugate().format_str())

    addCp = cp1 + cp2
    print("cp1 + cp2", addCp.format_str())
    subCp = cp1 - cp2
    print("cp1 - cp2", subCp.format_str())


if __name__ == '__main__':
    main()
