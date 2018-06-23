array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))


for row in range(N):
    array.append([])
    for column in range(M):
        if row + column == N - 1:
            array[row].append(1)
        else:
            array[row].append(0)


for row in array:
    print(row)