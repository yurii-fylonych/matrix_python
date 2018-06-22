array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)

min_el = array[0][0]

for i in range(N):
    for j in range(M):
        if array[i][j] < min_el:
            min_el = array[i][j]
            row_min_el = i
            column_min_el = j

print('Minimal element is {} and it is component location in ({},{}) position'.format(min_el, row_min_el, column_min_el))


for rows in array:
    print(rows)