# 3. Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

# my_list = (8, 2, 3, -1, 7)
# my_mulitply_list = 1
# for i in my_list:
#     my_mulitply_list*=i
   
# print(my_mulitply_list)

def my_list(numberss):
    my_mulitply_list = 1
    for i in numberss:
        my_mulitply_list*=i
    return my_mulitply_list
print(my_list((8, 2, 3, -1, 7)))