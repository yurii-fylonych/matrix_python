array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)

max_item = array[0][0]

for i in range(N):
    for j in range(M):
        if array[i][j] > max_item:
            max_item = array[i][j]

print('{} is maximal element in array.'.format(max_item))

for row in array:
    print(row)



