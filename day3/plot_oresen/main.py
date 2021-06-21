import datetime
import random
import string
import numpy as np
import matplotlib.pyplot as plt


def main(now: datetime) -> None:
    fig = plt.figure()

    ax = fig.add_subplot()

    # 折れ線グラフを出力
    left = np.array([1, 2, 3, 4, 5])
    height = np.array([100, 300, 200, 500, 400])
    ax.plot(left, height)

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
