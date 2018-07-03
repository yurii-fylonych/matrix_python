array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
   array.append([])
   for column in range(M):
       k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
       array[row].append(k)

max_aliquot_item = 0

for i in range(N):
   for j in range(M):
       if array[i][j] % 3 == 0 and array[i][j] > max_aliquot_item:
           max_aliquot_item = array[i][j]

if max_aliquot_item == 0:
    print('Absent value that aliquot to 3 in the matrix')
else:
    print('Maximal aliquot to 3 item in matrix equal to {}.'.format(max_aliquot_item))

for row in array:
   print(row)
