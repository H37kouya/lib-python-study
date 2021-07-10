import numpy as np


def main() -> None:
    # numpy配列の宣言
    n_list1 = np.array((10, 20, 30))
    print(n_list1)

    n_list2 = np.array((40, 50, 60))
    print(n_list2)

    # 配列の結合
    mergedNList = np.hstack((n_list1, n_list2))
    print(mergedNList)

    # 配列の四則演算
    print(n_list1 + 10)  # [20 30 40]
    print(n_list1 - 10)  # [ 0 10 20]
    print(n_list1 * 10)  # [100 200 300]
    print(n_list1 / 10)  # [1. 2. 3.]

    # 複素数の配列
    complex_list = np.array((
        1 + 2j,
        2 + 1j
    ))
    print(complex_list)

    # 一葉分布の乱数
    rand_list = np.random.rand(3)  # 0以上1.0未満
    print(rand_list)
    # 正規分布の乱数
    rand_normalized_list = np.random.randn(3)  # 平均0、分散1 (標準分布1)
    print(rand_normalized_list)

    print(np.eye(3))
    print(np.eye(2, 3))  # 2×3
    print(np.eye(3) + np.eye(3))

    invMatrix1 = np.linalg.inv(np.eye(3))
    print(invMatrix1)
    invMatrix2 = np.linalg.inv(np.array((
        (1, 2),
        (2, 1)
    )))
    print(invMatrix2)

    print(1e18)

    l2_1 = np.linalg.norm(np.array([1, 2, 3, 2, 1]), ord=2, axis=-1, keepdims=True)
    print(l2_1)
    l2_1[True] = 1
    print(l2_1)

    l2_2 = np.linalg.norm(np.array([1, 2, 3, 2, 1]), ord=2, axis=-1, keepdims=True)
    print(l2_2)
    l2_2[False] = 1
    print(l2_2)


if __name__ == '__main__':
    main()
