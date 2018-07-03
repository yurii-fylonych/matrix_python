import random
import math
import copy

class Matrix():
  """ Class to Create matrix """

  def __init__(self, N, M):
      """Initiate NXM matrix and choose the values borders a, b"""
      self.N = N
      self.M = M
      self.matrix = []

  def create_matrix_input(self):
      """Create matrix"""
      for row in range(self.N):
          self.matrix.append([])
          for column in range(self.M):
              k = int(input('Enter value in row № {}. Column is {}. Value = '.format(row, column)))
              self.matrix[row].append(k)

  def create_matrix_random(self, a, b):
      """Create matrix"""
      for row in range(self.N):
          self.matrix.append([])
          for column in range(self.M):
              self.matrix[row].append(random.randint(a, b))

  def swap_rows_up(self):
      """Change position of rows in matrix. Up + 1"""

      for i in range(self.M):
          for j in range(self.N - 1):
              self.matrix[j][i], self.matrix[j + 1][i] = self.matrix[j + 1][i], self.matrix[j][i]

      return self.matrix

  def count_number_double_digit_aliquot_2(self):
      """"Count number double digit items in which sum of digit aliquot to 2"""
      n = 0

      for i in range(self.N):
          for j in range(self.M):
              if self.matrix[i][j] > 10:
                  if (self.matrix[i][j] // 10 + self.matrix[i][j] % 10) % 2 == 0:
                      n += 1
      return n

  def get_average_nopositive_items_each_row(self):
      """"Calculate average values non-positive items in each matrix row"""
      average = []

      for i in range(self.N):
          sum = 0
          n = 0
          for j in range(self.M):
              if self.matrix[i][j] >= 0:
                  n += 1
                  sum += self.matrix[i][j]
          if n == 0:
              average.append(n)
          else:
              k = sum / n
              average.append(k)

      return average

  def count_number_negative_items_under_diagonal(self):
      """"Count number negative items under main diagonal of matrix"""
      n = 0

      for i in range(self.N):
          for j in range(self.M):
              if i > j and self.matrix[i][j] < 0:
                  n += 1
      return n

  def invert_matrixs_diagonals(self):
      """"Count number negative items under main diagonal of matrix"""
      k = math.ceil(self.N / 2)

      for i in range(k):
          for j in range(self.M):
              if i == j:
                  self.matrix[i][j], self.matrix[self.N - i - 1][self.M - j - 1] = self.matrix[self.N - i - 1][self.M - j - 1], self.matrix[i][j]
              if i + j == self.N - 1:
                  self.matrix[i][j], self.matrix[self.N - i - 1][self.M - j - 1] = self.matrix[self.N - i - 1][self.M - j - 1], self.matrix[i][j]

      return self.matrix

  def count_negative_values_in_columns(self):
      """Count negative items in each column"""
      number = []

      for i in range(self.M):
          n = 0
          for j in range(self.N):
              if self.matrix[j][i] < 0:
                  n += 1
          number.append(n)

      return number

  def count_positive_values_in_rows(self):
      """Count negative items in each column"""
      number = []

      for i in range(self.N):
          n = 0
          for j in range(self.M):
              if self.matrix[i][j] > 0:
                  n += 1
          number.append(n)

      return number

  def get_max_item(self, number):
      """Find a column, row with the maximum numbers of positive, negative items"""
      max_item = number[0]

      for index, item in enumerate(number):
          if item >= max_item:
              max_item = item
              max_item_index = index

      return max_item_index


  def get_min_item(self, number):
      """Find a column, row with the minimum_numbers of negative, positive items"""
      min_item = number[0]

      for index, item in enumerate(number):
          if item <= min_item:
              min_item = item
              min_item_index = index

      return min_item_index

  def print_matrix(self):
      """Print matrix"""
      for rows in self.matrix:
          print(rows)


matrix = Matrix(3, 3)
matrix.create_matrix_random(-20, 20)
matrix.print_matrix()
matrix.invert_matrixs_diagonals()
matrix.print_matrix()