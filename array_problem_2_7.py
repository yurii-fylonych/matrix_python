array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        if row == column:
            array[row].append(1)
        else:
            array[row].append(0)

for rows in array:
    print(rows)
