from playLA.LinearSystem import rank
from .Vector import Vector
from .Matrix import Matrix


def gram_schmidt_process(basis):
    matrix = Matrix(basis)
    assert rank(matrix) == len(basis)

    res = [basis[0]]
    for i in range(1, len(basis)):
        p = basis[i]
        for r in res:
            p = p - basis[i].dot(r) / r.dot(r) * r
        res.append(p)
    return res


def qr(A: Matrix):

    assert A.row_num() == A.col_num(), "A must be square"

    basis = [A.col_vector(i) for i in range(0, A.col_num())]
    P = gram_schmidt_process(basis)
    Q = Matrix([v / v.norm() for v in P]).T()
    R = Q.T().dot(A)

    return Q, R


# 求向量b在矩阵A的列空间上的投影
def least_squares(A: Matrix, b: Vector):
    # 求正交基
    basis = [A.col_vector(i) for i in range(0, A.col_num())]
    P = gram_schmidt_process(basis)

    res = Vector.zero(len(b))
    for p in P:
        res = res + b.dot(p) / p.dot(p) * p
    return res
