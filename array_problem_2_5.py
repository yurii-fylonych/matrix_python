
array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-20, 25))

for i in range(N):
    sum = 0
    for j in range(M):
        sum += array[i][j]
    print('Sum in ', i, ' row is ', sum)


for rows in array:
    print(rows)
