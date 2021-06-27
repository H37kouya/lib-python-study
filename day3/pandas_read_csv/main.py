import pandas as pd


def main() -> None:
    df = pd.read_csv('./normal_distribution.csv', header=None)
    print(df)

    nd = df.to_numpy()
    print(nd)


if __name__ == '__main__':
    main()
