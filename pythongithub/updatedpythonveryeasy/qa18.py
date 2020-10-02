#  Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :

# 3 -> [1, 5, 8, 3] : True

# -1 -> [1, 5, 8, 3] : False

value = [1, 5, 8, 3]
n = int(input("Enter a number: "))
if  n in value:
  print("True")
else:
  print("False")