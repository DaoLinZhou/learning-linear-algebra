import numpy as np
from scipy.linalg import svd


if __name__ == '__main__':

    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    # s不是奇异矩阵, 而是所有的奇异值
    U, s, VT = svd(A)
    print(U)
    print(s)
    print(VT)
    print()

    # 检验
    Sigma = np.zeros(A.shape)
    for i in range(len(s)):
        Sigma[i][i] = s[i]
    print(Sigma)
    print(U.dot(Sigma).dot(VT))


