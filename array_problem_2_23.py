array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))


for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-19, 20))

for i in range(N):
    sum_in_column = 0
    for j in range(M):
        sum_in_column += array[j][i]

    print('Items sum in {} column equal to {}.'.format(i, sum_in_column))


for row in array:
    print(row)