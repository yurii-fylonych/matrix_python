import random
import copy

array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-17, 26))

for row in array:
    print(row)

print('\t\t')
new_array = copy.copy(array)
for k in range(N):
    for i in range(M - 1):
        for j in range(M - 1):
            if new_array[i][j] > new_array[i + 1][j]:
                new_array[i][j], new_array[i + 1][j] = new_array[i + 1][j], new_array[i][j]

for i in new_array:
    print(i)
