array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))


for row in range(N):
    array.append([])
    for column in range(M):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)


for i in range(N):
    mult_items_in_row = 1
    for j in range(M):
        mult_items_in_row *= array[i][j]

    print('Items sum in {} row equal to {}.'.format(i, mult_items_in_row))


for row in array:
    print(row)
