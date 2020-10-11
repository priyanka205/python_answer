#    1) Write a Python program to sum of two given integers. 
#    However, if the sum is between 15 to 20 it will return 20.

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
x = int(input("Input X :"))

y = int(input("Input Y:"))

print(sum(x, y))
