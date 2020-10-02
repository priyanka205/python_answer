# Write a Python program to test whether all numbers of a list is greater than a certain number.


l = [215,25,75,63,96]
n = int(input("Enter a number: "))

for i in l:
  
  if i<n:
    print(f"{n} is  greater than {i}")
    break
else:
  print("All numbers given in list is greater than input")

    