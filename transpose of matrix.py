matrix = [[4, 6, 7, 8], [3, 7, 2, 7], [7, 3, 7, 5]]

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transpose(matrix))
