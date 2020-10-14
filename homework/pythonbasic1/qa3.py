
'''
3) Write a Python program which accepts a sequence of comma-separated 
    numbers from user and generate a list and a tuple with those numbers. 

Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

my_nums = input('give a string of comma separated numbers:' )
print(my_nums)
# print(type(my_nums))
my_list = my_nums.split(',')
print(my_list)