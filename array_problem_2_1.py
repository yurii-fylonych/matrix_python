


array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for rows in range(N):
    array.append([])
    for c in range(M):
        array[rows].append(random.randint(-20, 25))

for rows in array:
    print(rows)
