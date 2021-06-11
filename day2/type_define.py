from typing import Optional, Union


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
    if type(v) is str:
        return v

    return str(v)


if __name__ == '__main__':
    main()
