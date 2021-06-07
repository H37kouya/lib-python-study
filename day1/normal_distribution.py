import math


# メイン関数
def main():
    # listの初期化
    probability_list = list()  # 確率の配列

    # -3 -2.9 -2.8 ... 0 ... 2.8 2.9 3.0 の for loop
    for idx in range(-3 * 10, 3 * 10):
        val = idx / 10
        probability_list.append(normal_distribution(val))  # ここでlistに値を入れる
        print(val, ",", normal_distribution(val))
    print(probability_list)  # listの中身確認
    print(len(probability_list))  # listの要素数確認
    print(probability_list[28:33])  # listのスライス


# 標準正規分布
def normal_distribution(x: float) -> float:
    """
    標準正規分布

    f(x) = (1/sqrt(2pi))exp(-x^2/2)
    """

    # 係数
    coefficient = 1 / math.sqrt(2 * math.pi)
    # 指数
    exponent = math.exp(-(x ** 2) / 2)
    # 標準正規分布
    return coefficient * exponent


if __name__ == "__main__":
    main()
