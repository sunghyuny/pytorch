import numpy as np


def generate_random_array():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2], [3, 4], [5, 6]])

    C = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

    dot = np.dot(a, b)
    dot2 = np.dot(A, B)
    linalg = np.linalg.inv(C)
    det_C = np.linalg.det(C)
    print(dot, dot2)
    print(A.T)
    print(linalg,det_C)

generate_random_array()