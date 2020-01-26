from playLA.LinearSystem import LinearSystem
from playLA.LinearSystem import inv, rank
from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == '__main__':
    A1 = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A1, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()

    print()

    # 测试更加一般化的高斯约旦消元法
    A2 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b2 = Vector([1, 5, 13, -1])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()

    print()

    A3 = Matrix([[2, 2],
                 [2, 1],
                 [1, 2]])
    b3 = Vector([3, 2.5, 7])
    ls3 = LinearSystem(A3, b3)
    if not ls3.gauss_jordan_elimination():
        print("No solution")
    ls3.fancy_print()

    print()

    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(invA)
    print(invA.dot(A))
    print(A.dot(invA))

    print(rank(A1))


