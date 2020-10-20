
# 18) Given a following two sets find the intersection and remove those elements from the first set

# Expected Output:
# First Set  {65, 42, 78, 83, 23, 57, 29}

# Second Set  {67, 73, 43, 48, 83, 57, 29}

# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}
myfirst_set  = {23, 42, 65, 57, 78, 83, 29}
mysecond_set = {57, 83, 29, 67, 73, 43, 48}
my_list = myfirst_set.intersection(mysecond_set) #intersection


for x in my_list:
  myfirst_set.remove(x)
print(myfirst_set)
print(mysecond_set)
print(myfirst_set)
print(my_list)