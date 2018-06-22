array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)


for i in range(N):
    count = 0
    for j in range(M):
        if array[i][j] > 0:
            count += 1

    print(' In {} row {} positive (element bigger than zero) elements '.format(i, count))


for rows in array:
    print(rows)