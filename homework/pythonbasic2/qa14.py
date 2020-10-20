# 14) Given an input list removes the element at index 4 and add it to the 
# 2nd position and also, at the end of the list:
# For example: List = [54, 44, 27, 79, 91, 41]
# Expected Output:
# Original list  [34, 54, 67, 89, 11, 43, 94]
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
my_list = [34, 54, 67, 89, 11, 43, 94] 
print( my_list)

element_index = my_list.pop(4)
print(my_list)

my_list.insert(2, element_index)
print(my_list)

my_list.append(element_index)
print(my_list)








