#  Given a list of numbers. Iterate over all the numbers, 
#  divide all of them by 5 and save the answers (float value) in a list with ascending order.

def x():
    my_list = [1,2,3,4,5,6,7,8,9,10,15,25]
    my_list1 =[]

    for i in my_list:

        if i % 5 == 0:

            my_list1.append(i)

    return my_list1

print(x())   