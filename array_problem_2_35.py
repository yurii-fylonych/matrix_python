import random

matrix_1 = []
matrix_2 = []
r = []
matrix_mult = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    matrix_1.append([])
    for column in range(M):
        matrix_1[row].append(random.randint(-27, 38))

for i in range(N):
    matrix_2.append([])
    for j in range(M):
        matrix_2[i].append(random.randint(-27, 38))

k = 0

for i in range(N):
    for j in range(M):
        for a in range(M):
            k += matrix_1[i][a] * matrix_2[a][j]
        r.append(k)
        k = 0
    matrix_mult.append(r)
    r = []

for row in matrix_mult:
    print('\t\t', row)