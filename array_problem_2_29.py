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
       if array[i][j] > 0:
           count += 1
   number_positive_items.append(count)

number_of_min_items = number_positive_items[0]

for index, item in enumerate(number_positive_items):
   if item < number_of_min_items:
       number_of_min_items = item
       min_value = index

print('Row with minimum numbers of positive items is {}.'.format(min_value))

for row in array:
   print(row)