array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
   array.append([])
   for column in range(M):
       array[row].append(random.randint(-54, 61))

number_even_items = []

for i in range(N):
   n = 0
   for j in range(M):
       if array[i][j] % 2 == 0:
           n += 1
   number_even_items.append(n)

max_even_item = number_even_items[0]

for index, item in enumerate(number_even_items):
   if item > max_evem_item:
       max_evem_item = item
       row_with_max_even = index

print('Row with maximum even items is {}.'.format(row_with_max_even))

for row in array:
   print(row)