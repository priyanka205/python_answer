# 2. Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))


# my_list = [8, 2, 3, 0, 7]
# my_add_list = 0
# for i in my_list:
#     my_add_list += i
# print(my_add_list)

def sum(mylist):
    my_add_list = 0

    for i in mylist:
        my_add_list += i
        
    return my_add_list

print(sum((8, 2, 3, 0, 7)))