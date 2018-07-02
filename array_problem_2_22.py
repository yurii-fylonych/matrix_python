array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)

min_item = array[0][0]

for i in range(N):
    for j in range(M):
        if array[i][j] < min_item:
            min_item = array[i][j]

print('{} is minimal element in array.'.format(min_item))

for row in array:
    print(row)