array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))


for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-19, 20))

sum_items_second_diagonal = 0

for i in range(N):
    for j in range(M):
        if i + j == M - 1:
            sum_items_second_diagonal += array[i][j]

print('Sum items in secondary matrix s diagonal equal to {}.'.format(sum_items_second_diagonal))


for row in array:
    print(row)