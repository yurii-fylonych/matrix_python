array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))


for row in range(N):
    array.append([])
    for column in range(M):
        k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
        array[row].append(k)

count = 0

for i in range(N):
    for j in range(M):
        if array[j][i] % 2 == 0 and array[j][i] < 0:
            count += 1

print('Array has {} even and negative elements.'.format(count))


for row in array:
    print(row)
