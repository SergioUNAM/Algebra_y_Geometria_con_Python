"""The following functions presented perform standard operations on matrices: addition, multiplication by a number and transposition."""

"""Las siguientes funciones presentadas realizan operaciones estándares con matrices: suma, multiplicación por un escalar y transposición"""


def matrix_add(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[0 for j in range(len(A[0]))] for i in range(len(A))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] + B[i][j]

        return C
