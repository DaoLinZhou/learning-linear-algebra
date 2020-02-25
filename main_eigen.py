import numpy as np
from numpy.linalg import eig


if __name__ == '__main__':
    A1 = np.array([[4, -2],
                   [1, 1]])
    eigenvalues1, eigenvectors1 = eig(A1)
    print(eigenvalues1)
    print(eigenvectors1)
    print()

    A2 = np.array([[0, 1], [1, 0]])
    eigenvalues2, eigenvectors2 = eig(A2)
    print(eigenvalues2)
    print(eigenvectors2)
    print()

    A3 = np.array([[0, -1], [1, 0]])
    eigenvalues3, eigenvectors3 = eig(A3)
    print(eigenvalues3)
    print(eigenvectors3)
    print()

    A4 = np.array([[1, 0], [0, 1]])
    eigenvalues4, eigenvectors4 = eig(A4)
    print(eigenvalues4)
    print(eigenvectors4)
    print()

    A5 = np.array([[3, 1], [0, 3]])
    eigenvalues5, eigenvectors5 = eig(A5)
    print(eigenvalues5)
    print(eigenvectors5)
    print()
