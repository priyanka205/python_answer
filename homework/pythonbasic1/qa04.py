'''
4) Write a Python program that accepts an integer (n) and 
computes the value of n+nn+nnn. 

Sample value of n is 5
Expected Result : 615
'''

my_num = int(input('a single digit number: '))
my_num_b = str(my_num)*2
my_num_c = str(my_num)*3

print(my_num, my_num_b, my_num_c)

my_sum_is = my_num + int(my_num_b) + int(my_num_c)

print(my_sum_is)
