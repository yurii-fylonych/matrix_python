array = []


N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-35, 65))


for i in range(N):
    count = 0
    for j in range(M):
        if array[i][j] < 0:
            count += 1

    print(i, count)
