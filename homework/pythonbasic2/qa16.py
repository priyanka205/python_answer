# 16) Given a list iterate it and count the occurrence of each 
# element and create a dictionary to show the count of each element
# Expected Output:

# Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

my_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

my_count = dict()

for x in my_list:
    
  if(x in my_count):
    my_count[x] += 1
  else:
    my_count[x] = 1
  
print(my_count)