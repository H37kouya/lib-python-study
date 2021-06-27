import pandas as pd


def main() -> None:
    df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
    print(df.to_)
    #    a  b  c
    # 0  1  2  3
    # 1  4  5  6

    nd = df.to_numpy()
    print(nd)
    # [[1 2 3]
    #  [4 5 6]]


if __name__ == '__main__':
    main()
