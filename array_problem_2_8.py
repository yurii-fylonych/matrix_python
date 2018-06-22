array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(M):
    array.append([])
    for column in range(N):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)

counts_in_columns = []

for i in range(M):
    count = 0
    for j in range(N):
        if array[j][i] < 0:
            count += 1
    counts_in_columns.append(count)

min_items_in_row = 0

for index, item in enumerate(counts_in_columns):
    if item > min_items_in_row:
        column = index

print('The max numbers of negative items locate in {} column'.fornat(column))

for rows in array:
    print(rows)