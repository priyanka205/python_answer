Arrange String characters such that lowercase letters should come first.
Example:
Input: "aeiNPTvy"
Ouput: "yaivePNT"

my_list = "aeiNPTvy"
my_list2 = []
x = my_list[7]
y = my_list[6]
z = my_list[1]
a = my_list[4]
b = my_list[3]
my_list = x + my_list[0:2] + y + z + a + b 
print(my_list)





