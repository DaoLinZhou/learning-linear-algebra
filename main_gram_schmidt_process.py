from playLA.Vector import Vector
from playLA.GramSchmidtProcess import *


if __name__ == '__main__':
    basis1 = [Vector([2, 1]), Vector([1, 1])]
    res1 = gram_schmidt_process(basis1)
    for row in res1:
        print(row)
    res1 = [row / row.norm() for row in res1]
    for row in res1:
        print(row)
    print(res1[0].dot(res1[1]))
    print()

    basis2 = [Vector([2, 3]), Vector([4, 5])]
    res2 = gram_schmidt_process(basis2)
    res2 = [row / row.norm() for row in res2]
    for row in res2:
        print(row)
    print(res2[0].dot(res2[1]))
    print()

    # 测试最小二乘
    basis3 = Matrix([[-1, 1],
                     [1, 0],
                     [0, 1]])
    point = Vector([1, -2, 1])
    tr_point = least_squares(basis3, point)
    print(tr_point)
