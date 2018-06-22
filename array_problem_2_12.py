array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)

i = 0
j = 0

for i in range(M):
    count = 0
    for j in range(N):
        if array[j][i] > 0:
            count += 1
    print(i, count)