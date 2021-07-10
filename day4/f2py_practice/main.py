import f2
import numpy as np

if __name__ == '__main__':
    ix = 5
    qq = np.zeros(ix) # 適当にnumpy配列を定義
    print(qq)
    qq_add = f2.add(qq,ix) # f2pyで定義した関数を呼び出す
    print(qq_add)
