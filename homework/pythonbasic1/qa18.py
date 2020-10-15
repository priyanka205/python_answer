# 18) Given a range of numbers. Iterate from 0th 
# number to the end number and print the sum of the current number and previous number.

# [88,55,92,4,45,25,31,97,85]

my_numbers = [88,55,92,4,45,25,31,97,85]
for i in  (my_numbers+1):
    print(i + my_numbers)


