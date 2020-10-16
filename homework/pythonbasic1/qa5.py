

# 5) Write a Python program to get the difference between a given number and 17, if the number 
# is greater than 17 return double the absolute difference.

def my_list(x):
    if x <= 17:
        return 17 - x
    else:
        return (x - 17) * 2 

print(my_list(25))
print(my_list(9))