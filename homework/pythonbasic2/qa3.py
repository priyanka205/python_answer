
# 3) Given a two list of ints create a third list such that 
# should contain only odd numbers from the first list and even numbers from the second list.

# Example: 
# listOne = [10, 20, 23, 11, 17] #ODD Number
# listTwo = [13, 43, 24, 36, 12] #even number
# Merged List is
# [23, 11, 17, 24, 36, 12]

listone = [10, 20, 23, 11, 17]
listtwo = [13, 43, 24, 36, 12]
listthird = []
for i in listone:
    if  i % 2 == 1:
        listthird.append(i)
for j in listtwo:
    if j % 2 == 0:
        listthird.append(j)

print(listthird)





   
