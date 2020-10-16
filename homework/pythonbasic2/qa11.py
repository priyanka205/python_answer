#  Find all occurrences of “USA” in given string ignoring the case
# Expected Outcome:
# input_str = "Welcome to USA. usa awesome, isn't it?"
# The USA count is: 2

input_str = ("Welcome to USA. usa awesome, isn't it?")
my_list = input_str.split(" ")
print(my_list)
listof_usa = []
for x in my_list:
    if "usa" in x.lower():
        listof_usa.append(x)
print(listof_usa) 
print(len(listof_usa))   



# for x in input_str:
#     if x.isupper() or x.isupper() :
#         my_list.count("usa")
# print(my_list)

     