import datetime
import random
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main(now: datetime) -> None:
    # データの取得
    normal_distribution_list = fetch_data()

    # データの加工
    x_values = normal_distribution_list[:, 0]
    y_values = normal_distribution_list[:, 1]

    # グラフのプロット
    do_plot(
        x_values=x_values,
        y_values=y_values,
        now=now
    )


def fetch_data() -> np.ndarray:
    # CSVの取得
    df = pd.read_csv('./normal_distribution.csv', header=None)
    print(df)

    # numpyに変換
    nd = df.to_numpy()
    print(nd)
    return nd


def do_plot(x_values, y_values, now: datetime) -> None:
    # グラフのプロット
    fig = plt.figure()

    ax = fig.add_subplot()

    # 折れ線グラフを出力
    ax.plot(x_values, y_values)

    fig.savefig(f'{generate_file_name(now)}.png', facecolor=fig.get_facecolor())


def generate_file_name(now: datetime) -> str:
    """
    ファイル名の生成

    :param now: 現在時刻
    :return:
    """
    return f'{now.strftime("%Y%m%d_%H%M%S")}_{random_str(4)}'


def random_str(length: int) -> str:
    """
    ランダムな文字列を生成

    :param length: 文字数
    :return:
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


if __name__ == '__main__':
    dt_now = datetime.datetime.now()
    main(now=dt_now)
