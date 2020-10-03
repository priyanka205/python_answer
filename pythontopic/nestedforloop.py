# *
# * *
# * * *
# * * * * *
# * * * * * *

# limit = int(input("Enter a range number: "))
# for i in range(limit):
#     for j in range(i+1):
#          print("*", end = "")
#         #  print("*")    
#     print("\n")



#        *

#      * * *

#    * * * * *

limit = int(input("Enter a range number: "))
space = limit
for i in range(limit):
    print(" "*space, end=" ")
    for j in range(i+1):
        print("*", end = " ")   
    space -= 1 
    print("\n")

# limit = int(input("Enter a range number: "))
# space = limit
# for i in range(limit):
#     if i%2 != 0:
#         continue
#     print(" "*space, end=" ")
#     for j in range(i+1):
#         print("*", end = " ")   
#     space -= 1 
#     print("\n")











