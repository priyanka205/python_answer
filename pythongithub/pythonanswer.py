#QA1:

#mypoem = """Twinkle, twinkle, little star,
  #How I wonder what you are!
     #Up above the world so high,
#     # Like a diamond in the sky
# #Twinkle, twinkle, little star,
#    #How I wonder ahat you are"""
# #print(mypoem)


# #QA2:

# #firstname = input("Priyanka")
# #lastname = input("Shrestha")
# #print( lastname + " " + firstname)

# #QA3:

# #QA4

# #color_list =["Red","Green","White","Black"]
# #print(color_list[0],color_list[-1])


# #QA:6

# #def sum_numbers(a,b,c):
#    #sum = a+b+c
#    #if a==b==c:
#       ##return sum*4
# ##print(sum_numbers(5,5,5))
# #print(sum_numbers(1,2,3))





# #QA7:
# #input is as follows:
# #color_list = ["Red","Green","White" ,"Black"]


# #expected output:
# # color_str = "Red Green White Black" 

# #color_str = " ".join(color_list)
# #print(color_str)

# #QA8:

# # # #height = int(input("give height: "))

# # # base = int(input("give base: "))
# # # area = height*base*0.5
# # # print(area)


# # #QA9:
# # #  Write a Python program to solve (x + y) * (x + y). 
# # # Test Data : x = 4, y = 3
# # # Expected Output : (4 + 3) ^ 2) = 49

# # # x = int(input("give x: "))
# # # y = int(input("give y: "))
# # # # x = 4
# # # # y = 3
# # # expt_out = (x + y)**2
# # # print(expt_out)

# # # qa10:
# # # follow this link to get idea on the calculation
# # # https://www.wikihow.com/Find-the-Distance-Between-Two-Points#:~:text=%20Steps%20%201%20Take%20the%20coordinates%20of,y1%20to%20find%20the%20vertical%20distance.%20More%20
# # # https://www.mathsisfun.com/algebra/distance-2-points.html



# # #QA11:
# # # follow this link to get the conversion scale:
# # # https://www.calculatorsoup.com/calculators/conversions/height-ft-and-in-to-cm.php

# # # x_ft = int(input("give ft:"))
# # # y_in = int(input("give in:"))
# # # # cm_value 
# # # # conversion
# # # x_cm = x_ft*30.48
# # # y_cm = y_in*2.54
# # # total_cm = x_cm + y_cm
# # # print(total_cm)

# # # QA:12

# # # a = int(input("give a: "))
# # # b = int(input("give b: "))
# # # c = (a**2 + b**2)**0.5
# # # print(c)

# # # # QA:13
# # # x = int(input("given number: "))
# # # total = 0
# # # while(x>0):
# # #    d = x % 10
# # #    total = total + d
# # #    x=x//10
# # # print("Sum of int: ",total)

# # # QA:15 switching the variables:
# # #this one using another variable
# # a = 5
# # b = 10
# # # # a = b
# # # # b = a
# # # # print(a)
# # # # print(b)
# # # #here we have lost the value of a:
# # # temp = a
# # # a = b
# # # b = temp
# # # print(a)
# # # print(b)
# # # or we can use this way too,without creating third variable:
# # a,b = b,a
# # print(a)
# # print(b)

# # QA16:string method isnumeric() checks whether the string consists of only numeric characters.
# # This method is present only on unicode objects.
# # to define a sting as unicode , one simply prefixes a "u" to the opening quotation mask of the assignment.

# # x = u"priyanka";
# # print(x.isnumeric())

# # x = u"742";
# # print(x.isnumeric())

# # Qa:17 to test whether a passed letter is a vowel or not.
# # vowels: a,e,i,o,u,A,E,I,O

# # ch = input("given value: ")
# # if (ch=="a" or ch=="e" or ch=="i" or ch=="o"or ch=="u" or ch=="A" or 
# # ch=="E" or ch=="I" or ch=="O" or ch=="U"):
# #   print(ch, "this are a vowel")
# # else:
# #    print(ch, "this are  not a vowel")

# # QA:19


# # numbers = [    

# #     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 

# #     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 

# #     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 

# #     958,743, 527

# #     ]
# #to get numbers before 237 is seen and is even:
# # for x in numbers:
# #    if x == 237:
# #       break
# #    elif x % 2 == 0:# % returns the reminder
# # #       print(x)

# #to get numbers that are even and are less than 237
# # for x in numbers:
# #    if x >= 237:
# #       continue
# #    elif x % 2 == 0:
# #       print(x)
   
      



# # # QA21:
# # value = int(input("given name: "))
# # if value > 0:
# #    print(value, "is posative")
# # elif value == 0:
# #    print(value, "is zero")
# # else:
# #    print(value, "is negative")

# #QA:22

# 4 | 29 |7.25
#     28
#     ----
#     10
#     8
#     20
#     20
#     0

# 29%4
# 29//4


#single / gives full divisine with decimel points
#// gives quotioned of the full divison after removing the decimal points
#% gives the reminder if the divison is not exact.


#QA:22

# numbers = [2,15,19,25,60,45,38]
# for x in numbers:
#    if x % 15 == 0:
#       print(x)
#    else:
#       print(x, "is not divisible")

#QA24:

# a = 2
# b = 2
# c = 4
# output = 9

# a = 2
# b = 2
# c = 4
# output = 0

# if a == b:
#    print(0)
# elif b == c:
#    print(0)
# elif c == a:
#    print(0)
# else:
#    print(a+b+c)  

# QA:14:Write a Python program to test whether all numbers of a list is greater than a certain number
# l = [215,25,75,63,96]
# n = int(input("Enter a number: "))

# for i in l:
  
#   if i<n:
#     print(f"{n} is  greater than {i}")
#     break
# else:
#   print("All numbers given in list is greater than input")


# 18) Write a Python program to check whether a specified value is
#  contained in a group of values.

# Test Data :

# 3 -> [1, 5, 8, 3] : True

# -1 -> [1, 5, 8, 3] : False

# value = [1, 5, 8, 3]
# n = int(input("Enter a number: "))
# if  n in value:
#   print("True")
# else:
#   print("False")



















