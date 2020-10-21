# 18) Given a range of numbers. Iterate from 0th 
# number to the end number and print the sum of the current number and previous number.

# [88,55,92,4,45,25,31,97,85]

my_number = [88,55,92,4,45,25,31,97,85]
prev_number = 0
for n, data in enumerate(my_number):
    if n>0:
        sum = prev_number+data
        print(sum)
    else:
        prev_number = data
        continue
    prev_number = data


