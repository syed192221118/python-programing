def multiply_matrices(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[2, 1], [3, 4]]
B = [[31], [1, 2]]
C = multiply_matrices(A, B)
print(C)  # Output: [[7, 4], [13, 11]]
