# Write a Python function that takes a positive integer and returns
#  the sum of the cube of all the positive
#  integers smaller than the specified number.


def sum_of_cubes(x):
  x -= 1
  total = 0
  while x > 0:
    total += x * x * x
    x -= 1
  return total
print(sum_of_cubes(5))