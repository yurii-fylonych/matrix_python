array = []

N = int(input('Enter number of rows = '))
M = int(input('Enter number of columns = '))

for row in range(N):
   array.append([])
   for column in range(M):
       array[row].append(random.randint(-27, 43))

number_aliquot = []

for i in range(N):
   n = 0
   for j in range(M):
       if array[j][i] % 5 == 0:
           n += 1
   number_aliquot.append(n)

max_aliquot = number_aliquot[0]

for index, item in enumerate(max_aliquot):
   if item >= max_aliquot:
       max_aliquot = item
       column = index

print('Column with maximum aliquot items to 5 is {}.'.format(column))

for row in array:
   print(row)
