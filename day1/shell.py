import random

MAX_LOOP = 1000000   # ループ数
MIN_RAND_NUMBER = 1  # 最小のランダムな数
MAX_RAND_NUMBER = 4  # 最大のランダムな数

# ランダムな数字のリスト作成
results = list()
for _ in range(0, MAX_LOOP):
    results.append(random.randint(MIN_RAND_NUMBER, MAX_RAND_NUMBER))

# ランダムな数が何回出たかをカウントするためのリストの初期化
counts = list(range(MAX_RAND_NUMBER + 1))
for countIdx in range(MIN_RAND_NUMBER, MAX_RAND_NUMBER + 1):
    counts[countIdx] = 0

# 集計
for resultIdx in range(0, MAX_LOOP):
    countIdx = results[resultIdx]
    counts[countIdx] += 1

# 出力
for countIdx in range(MIN_RAND_NUMBER, MAX_RAND_NUMBER + 1):
    print(str(countIdx) + ", " + str(counts[countIdx]))
