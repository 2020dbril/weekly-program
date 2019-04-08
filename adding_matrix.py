def matrix_addition (a, b):
    for n in range(len(a)):
        for m in range(len(a[0])):
            b[n][m] = a[n][m] + b[n][m]
    return b
x = [[1,2,3],[2,3,4]]
y = [[2,3,4],[1,1,1]]
print(matrix_addition(x, y))
