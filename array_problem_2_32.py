array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
    array.append([])
    for column in range(M):
        array[row].append(random.randint(-65, 45))

i = 0
j = 0

while i < N:
    while j < M:
        if array[i][j] % 2 == 0:
            min_even = array[i][j]
            break
        else:
            j += 1
    i += 1

for i in range(N):
    for j in range(M):
        if array[i][j] % 2 == 0 and array[i][j] < min_even:
            min_even = array[i][j]

print('Minimal even item in array equal to {}.'.format(min_even))

for row in array:
    print(row)