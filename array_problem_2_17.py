array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

k = 1

for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(column + 1)


for row in array:
    print(row)