array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-67, 23))

max_item = array[0][0]

for i in range(N):
    for j in range(M):
        if array[i][j] > max_item:
            max_item = array[i][j]
            x, y = i, j

print('{} is maximal element in array. It locate in position {}, {}.'.format(max_item, x, y))

for row in array:
    print(row)
