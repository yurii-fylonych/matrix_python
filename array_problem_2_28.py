array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
   array.append([])
   for column in range(M):
       k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
       array[row].append(k)

number_positive_items = []

for i in range(N):
   count = 0
   for j in range(M):
       if array[j][i] > 0:
           count += 1
   number_positive_items.append(count)

column_with_min_sum = number_positive_items[0]

for index, item in enumerate(number_positive_items):
   if item < column_with_min_sum:
       column_with_min_sum = item
       index_of_column_ = index

print('Column with minimum numbers of positive items is {}.'.format(index_of_column))

for row in array:
   print(row)