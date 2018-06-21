array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-20, 25))

min_el = array[0][0]

for i in range(N):
    for j in range(M):
        if array[i][j] < min_el:
            min_el = array[i][j]

print('Minimal value in {}X{} matrix is {}'.format(N, M, min_el))


for rows in array:
    print(rows)
