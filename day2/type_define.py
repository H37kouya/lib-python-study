from typing import Optional, Union, List


def a(d: List[int]) -> None:
    """
    python3.8まで

    importする必要がある
    """
    print(d)


def a(d: list[int]) -> None:
    """
    python3.9

    importする必要がなくなった
    """
    print(d)


def main() -> None:
    num: int = 10
    name: str = "タケシ"

    print(num, name)


def format_name(
        first_name: str,
        last_name: str,
        middle_name: Optional[str]
) -> str:
    if middle_name is None:
        return first_name + " " + last_name

    return first_name + " " + middle_name + " " + last_name


def convert_to_str(v: Union[int, str]) -> str:
    if isinstance(v, str):
        return v

    return str(v)


if __name__ == '__main__':
    main()
