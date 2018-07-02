array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))


for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-19, 20))

mult_items_in_diagonal = 1

for i in range(N):
    for j in range(M):
        if i == j:
            mult_items_in_diagonal *= array[i][j]

print('Multiplication items in matrix s diagonal equal to {}.'.format(mult_items_in_diagonal))


for row in array:
    print(row)
