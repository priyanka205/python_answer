#practice of list 

#mylist = ["apple" , "banana" , "orange"]
#mylist.append("peach")
#print(mylist)


#s = "priyanka shrestha"
#print(s)


#thistuple =("apple", "orange" , "banana")
#print(thistuple)

#Access Tuple items
#you can access tuple items by referring to the index number, inside square brackets:
#thistuple = ("banana" ,"apple" , "orange")
#print(thistuple[1:3])

#negativeindex: Negative indexing means begining from the ebd, -1 refers to the last item -2 refers to the second last item.

###thistuple =("apple", "orange", "banana")
#print(thistuple[-2])

#Range of index: 
#we ca specify a range of indexes by specifying where to start and where to end the range
#when specifying a range, the return value will new tuple with specified itmes
#example:Return the third,fourth, and fifth item.

##thistuple = ("apple", "banana", "ornage", "peach", "potato")
#print(thistuple[1:4])

#Range of negative index
# negative indexes if you want to start the search from the end of the tupel:
#thistuple = ("apple", "banana", "ornage", "peach", "potato")
#print(thistuple[-4:-2])

#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4(included) to index -1 (excluded)
#the last has the index -1

#change tuple values:
#Once tuple is create, you cannot change its value. Tuples are inchangeable or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list and convert the list back into a tuple


#Example: convert the tuple into a list to be able to change it:

#x = ("apple", "banana", "ornage")
#y = list(x)
#y[1] = "kiwi"
#x = tuple(y)
#print(x)

#Loop through a tuple 
#we can loop through the items the tuple items by using a for loop.

#example: Iterate through the items and print the values:



#myname = ("priyanka" ,"priya", "Bishwa", "menaka")
#for y in myname:
    #print(y)


#check if "bishwa is present in the tuple"

#mytuple = ("priyanka", "bishwa", "priya", "kiran", "menaka")
#if "priya" in mytuple:
   # print(yes, she is there!)


#tuple lenght: to determine how many items a tuple has, the len() method:



#x = ("priya","priyanka")
#print(len(x))


#add item:

#
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# Create  a tuple with only one item, you have to add a comma(,) after item, otherwise python will not recognize it is as tupe.

#thistuple = ("priyanka",)
#print(type(thistuple))

#thistuple = ("priyanka")
#print(type(thistuple))


#removes item: we cannot change item in tuple:
#tuple are unchangeable, so you cannot remove items from it but you can delete the tuple completely


#the tuple  keyword can delete completely

#join two tuples:
#to join two or more tuples you can use the + operator:


#The tuple () Cinstructor:

#It is also possible to use the tuple() constructor to make a tuple
#using the tuple() method to make a tuple:
#thistuple = (("priyanka", "priya", "bishwa"))
#print(thistuple)

#set
#thislist = {"priyanka","priya","bishwa"}
#for x in thislist:
    #print(x)



#thislist = {"priya","priyanka","bishwa","punam"}
#print(thislist)


#thislist = {"priyanka","priya","bishwa"}
#if "priyanka" in thislist:
    #print("yes, she is there")

#x = {"apple","banana","peach"}
#x.update(["orange","grapes"])
#print(x)


#x = {"shrestha","gopali","giri"}
#print(len(x))

#remove and discard method:

#x = {"priya","tisa","priyanka","prima","bhaivab","arnav"}
#x.remove("arnav")
#print(x)
#x = {"priya","tisa","priyanka","prima","bhaivab","arnav"}
#x.discard("arnav")
#print(x)
#if condition
#a = 33
#b = 200
#if b > a:
   # print("b is greater than a")


# #elif:this metion that if upper conditon is not true then try this one
# '''
# a = 55
# b = 55
# if a>b:
#     print("a is greater than b")
# elif a == b:
#     print("a and b are equal")


#else
'''
a = 105
b = 55
if a<b:
    print("b is greater than a")
elif a<b:
    print("a is not greater tham b")
else:
    print("a is greater than b")
    '''


#If you have only one statement  to exute,one for it, and one for else you can put it all on the saem

#a = 2
#b =330
#print("A") if a > b else print("B")


#one line if statement is 3 conditons:
# a = 330
 #b =330
#print("A" if a>b else print("=") if a == b else print("B")

#and:The and keyword is a logical operator, and is used to  combine conditonal statements:

#a = 200
#b = 53
#c =900

#if a>b and c>a:
    #print("Both statments are true")


#or: The or keyword is a logical operator, andis used to combine conditonal statments:
'''
a = 50
b = 40
c = 900

if a>b or a>c:
    print("At least one conditon is correct")
    '''



#nested if: you can have if statement inside if statement, this is called nested if statment:
'''
x = 51
if x > 10:
    print("Avobe ten,")
    if x > 20:
        print("and aslo above 20")
    else:
       print("x is greater than enything else")   
       '''


  #the pass statment:
  # #if statment cannot be empty, but if you for some reason have id atametn with no content, put in the pass statmetn to avoid getting an error.


    #Python for loops: python for loops 
    # A for loop is used for iterating over a sequance(that is either a list, a tuple, a dictionary, a set, or a string)
    # this is less like the for keyword in other programming languages, and works more like an iterator method as found on other object-orined programming language;
    #with the for loop we can excute a set of statemtns, once for each item in list, tuple, set etc.
      

#print each fruits in a fruit list:
'''
fruits = ["banana","apple","orange","peach"]
for x in fruits:
    print(x)
    '''

#for loop does not require an indexing variable to set beforehead.
#looping through string:
#even  strings are iterable objects, they contain a sequence of characters:

#loop through the letters in the word "banana":

#break:with the break statment we can stop the loop before it has looped through all the items:

#b = "bananna"
##print(x)
#fruits = ["apple", "banana","cherry","grapes","orange"]
#for y in fruits:
    ### break


    
#fruits = ["apple","ball","cat","dog"]
##print(x)
    #break


#the continous statment we can stop the current iteration of the loop, anf continue with the next:
#do not print banana:
#fruits = ["apple","bananan","orange"]
#for x in fruits:
    #if x == "orange":
       # break
    #print(x)
#range() function to loop a set of code a specified numbers of times, we can use the range() function,THe range range() function returns a sequence of numbers startion from 0 default, and increatmetn by 1 
#


#range
#for x in range (10):
#print(x) note that range(10) is not values of 1 to 10, its o to 9.

# The range () function defaults to 0 as a starting va,ue, however it is specify the starting value by adding a parameter: range(2, 6),whcih means value from 2 to 6 (but not including 6)

 

#for x in range(4, 9):
# print(x)



#for x in range(3, 25, 2):
# print(x)

#else in for loop:
#The else keyword in aa for loop specifes a block of code to be excuted when the loop is fincished:


'''
for x in range(3, 105, 2):
    print(x)
else:
    print("finally finsihed")
'''


#nested loops:
#a nested loop is a loop iside a loop.
#The inner loop will be excuted one time for each iteration of the outer loop

'''
fruits = ["apple","banana","orange","peach"]
car = ["tesla","honda",]
for x in fruits:
    for y in car:
        print(x,y)
'''

#Pass Statment:
#For loos cannot be empty, but if you for some reason a for loop with no content, put in the pass statment to avoid getting an error:

#for x in [0,1,1]:
#pass

#indexing slicing stepping:
#l1= [3,4,5,6,3,6,32]
#l2= [7,4,9,5,3,4,6,3]
#print(l1[0])
#print(l1[3])

#negative index:
#l1= [3,4,5,6,3,6,32]
#print(l1[-2:-1])

#l1= [3,4,5,6,3,6,32]
#print(l1[:5])
#stepping
#l1= [3,4,5,6,3,6,32]
#print(l1[0:-4])

# name = "priyanka"
# x = name.capitalize()
# print(x)

# my_favourite = "I love fruits, at the same time all love rice, but I often like to have fruits"
# x = my_favourite.count("fruits")
# print(x)


# name = "my name is priyanka, I am from Nepal"
# x = name.index("priyanka")
# print(x)

# using strip:it removes spaces
# my_name = "llllll    priyanka     "
# x = my_name.strip(" ,.l")
# print(x)


# github command:https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html#:~:text=%20%20%20%20Git%20task%20%20,clone%20username%40host%3A%2Fpath%2Fto%2Freposit%20...%20%2013%20more%20rows%20

#Dictionary:A dicitionary is a collection whcih is unordered, changeable and indexed. In python dictionaries are written with curly brackets, and they have keys and values.
# this_dict = {"name": "Priyanka", "age": 26}
# print(this_dict)

# #  items:we can access the accessingitems or a dictionary by refering to its key name,inside square brackets:
# this_dict = {
#     "my_name": "priyanka",
#     "my_lastname": "Shrestha",
#     "my_height": 160,
#     "my_weight":55
# }
# for x , y in this_dict.items():
#     print(x, y)

#if
# this_dict = {
#     "my_name": "priyanka",
#     "my_lastname": "Shrestha",
#     "my_height": 160,
#     "my_weight":55
# }
# if "my_height"   in this_dict:
#     print("yes, its there!")

# this_dict = {
#     "my_name": "priyanka",
#     "my_lastname": "Shrestha",
#     "my_height": 160,
#     "my_weight":55
# }
# print(len(this_dict))

#adding new keys and value:
# this_dict = {
#     "my_name": "priyanka",
#     "my_lastname": "Shrestha",
#     "my_height": 160,
#     "my_weight":55
# }
# this_dict["origin"] = "Nepal"
# this_dict["Mother's name"] = "Menaka"
# print(this_dict)

# pop is for removing keys
# this_dict = {
#     "my_name": "priyanka",
#     "my_lastname": "Shrestha",
#     "my_height": 160,
#     "my_weight":55
# }
# this_dict.pop("my_height")
# print(this_dict)

# while loop:

# i = 0
# while i<= 10:
#     i += 1
#     if i == 212:
#         continue
# print(i)

#l1= [3,4,5,6,3,6,32]
#l1[1]=20
#print(l1)



#a = [1,2,3,4,5,6]
#b = ["priyanka"]
#a.sort(reverse=True)
#print(a)
#b.sort(reverse=True)
#print(dir(b))




#condition:

#a = -30
#if a%5 == 0 or a%2 == 0:
    #print("It is  divisble by 2 and 5")
#else:
    #print("Its not divisibe by 2 and 5")

   

#nested if else:
'''
a = -30
if a%5 == 0:
    if a%2 == 0:
        print("it is divisible")
    else:
        print("it is not divisible")
else:
    print("whatever")
    '''

'''
a = 30
if a>0:
    print("a is posative number")
else:
    print("a is negative numbe")

    '''
'''
cars = ["tesla","honda","nissan","ford"]
new_car = "lamborgani"
if new_car not in cars:
    cars.append(new_car)
else:
    print("lamborgani is in the list")
print(cars)#  imp
'''

#for loop in list
'''
fruits = ["apple","banana","orange","peach"]
for x in fruits:
    print(x)
        '''
'''
fruits = ["apple","banana","orange","peach"]
for f in fruits[1]:
    print(f)
'''

#a =5
#b =6
#c =a+b
#print(a+b)

# print(" Twinkle, twinkle, little star,")
# print("\t How I wonder what you are!")
# print("\t\t  Up above the world so high,")
# print("\t\t Like a diamond in the sky")
# print("Twinkle, twinkle, little star,")
# print("\t How I wonder what you are")


# Write a Python program which accepts the user's first and last name and print them in
#  reverse order with a space between them.

# first_name = input("Enter a name: ")
# last_name = input("Enter a name: ")
# reverse_name = last_name + " " + first_name
# print(reverse_name)


# 3) Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java


# filename = "learning.py"
# sample = filename.split(".")
# x = sample[-1]
# print(x)






# 4) Write a Python program to display the first and last colors from the following list. 

# color_list = ["Red","Green","White" ,"Black"]
# # my_list = color_list[0],color_list[-1]
# # print(my_list)

# print(color_list[0],color_list[-1])



#  Write a Python program to concatenate all elements in a list into a string and return it.

# My_family = ["Priyanka","Priya","Bishwa","Menanka"]
# my_list = " ".join(My_family)
# print(my_list)
# print(type(my_list))




#  Write a Python program that will accept the base and height of a triangle and compute the area.

# height = int(input("Enter height: "))
# base = int(input("give base:"))
# area = height*base*0.5
# print(area)

# Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

# x = 3
# y = 3
# z = (x + y)**2
# print(z)

#  Write a Python program to convert height (in feet and inches) to centimeters. 

# feet = int(input("Enter feet: "))
# inches = int(input("Enter inches: "))
# centi = feet*30.48 + inches*2.54
# print(centi)

# Write a Python program to calculate the hypotenuse of a right angled triangle.


# a = int(input("Given number:"))
# b = int(input("Given number: "))
# c = (a**2 + b**2)**0.5
# print(c)

#  Write a Python program to calculate the sum of the digits in an integer.

# x = int(input("Given number:"))
# y = int(input("Given number: "))
# z = x + y
# print(z)
# print(type(z))
# n = input("Enter a number: ")
# sum = 0
# for i in n:
#     sum+=int(i)
# print(sum)

# Write a Python program to test whether all numbers 
# of a list is greater than a certain number.

# my_list = [5,10,45,75,78,15]
# certain_number = int(input("Enter a number:"))
# for i in my_list:
#     if i<certain_number:
#         print(f"{certain_number} is greater than {i}")
#         break
# else:
#      print("All numbers given in list is greater than input")
# Write a Python program to swap two variables.

# a = 10
# b = 5
# a = b 
# b = a
# print(a)
# print(b)

# Write a Python program to check if a string is numeric.

# my_list = u"125";
# print(my_list.isnumeric())


#  Write a Python program to test whether a passed letter is a vowel or not.
# list = ("a","e","i","o","u")
# ch = input("given value: ")
# for i in list:
#     if ch == i or ch == i.upper():
#         print(ch, "this is a vowel")
#         break
    # # if ch == i.upper():
    #     print("this is a vowel")
    #     break
# else:
#     print(ch, "this is not a vowel")  
# Write a Python program to check whether a specified value is contained in a group of values. (     Doubt)
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# data = [1, 5, 8, 3]
# for i in data:
#     if i == 7:
#         print("True")
#         break
# else:
#     print("false")




# data = [1, 5, 8, 3]
# n = int(input("Enter number: "))
# if n in data:
#     print("True")
# else:
#     print("False")



# numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527 ]
# for x in numbers:
#     if x == 237:
#         break
#     elif x % 237 == 0:
#          print(x)
       
# write a Python program to divide a path on the extension separator.
# path = ("priyanka.py")
# my_path = path.split(".")
# print(my_path[-1])
       
# filename = "https://www.practice.com.py"
# my_file = filename.split(".")
# new = my_file[0:-1]
# req = "." .join(new)
# print(req)
# Write a Python program to check if a number is positive, negative or zero.

# check_num = int(input("Enter number: "))
# if check_num > 0:
#     print("it is posative")
# elif check_num == 0:
#     print("its a zero")
# else:
#     print("its a negative")

# e a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# a = 5
# b = 5
# c = 7


# a = 4
# b = 1
# c = 8

# if a == b:
#    print(0)
# elif b == c:
#    print(0)
# elif c == a:
#    print(0)
# else:
#    print(a+b+c)  

# n = int(input("Enter a number: "))
# for i in range(0,n):
#     for j in range(i+1):
#         print("*", end = " ")
#     print("\n")



# for i in 'abc':
#     print(i)
#     for j in '123':
#         print(j)
#     for k in r"&#@":
#         print(k)

# def my_function():
#     print("My name is Indraman")
# # my_function()

# def my_function(fname):
#     print(fname + " Gopali")
# my_function("Indra Man")
# my_function("Chandrakala")
# my_function("Ivan")

# def my_function(fname,lname,Age):
#     print(fname + " " + lname + " " + Age)
# my_function("Priyanka","Shrestha","Thirty")

# def my_function(**kid):
#     print("My youngest child  name is " + kid["fname"])
# my_function(fname="Ivan",lname=("shrestha"))

# def my_function(child1,child2,child3):
#     print("Mummy's favourite child is " + child1)
# my_function(child2="Priya",child3="Priyanka",child1="Bimej.")

# def my_function(country= "Nepal"):
#     print("I am from "+ country)
# my_function("USA")
# my_function


# def my_function(food):
#   for x in food:
#     print(x)

# fruit = ["apple", "banana", "cherry"]

# my_function(fruit)

# def my_function(x):
#     return x * 5
# print(my_function(5))

# def my_function():
#     pass

# x =10
# def add(y):
#     global x
#     x =20
#     print(x+y)
# add(5)
# print(x)

# x = 10
# y = 20
# z = 30

# def add(p):
#     global x, y, z
#     x = 1
#     y = 2
#     z = 3
#     print(x+y+z+p)
# add(5)
# print(x)
# print(y)
# print(z)

# def greet():
#     print("HEllo priyanka")
#     greet()
# greet()

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())


# n = round(20.5623,3)
# print(n)
# import math
# num = 256.2565666
# nu = math.ceil(num)
# print(nu)

# x = 255.454548
# n = math.floor(x)
# print(n)

# import random
# n = random.randrange(25)
# print(n)

# import random
# n = random.shuffle(25,5,46,4545)
# print(n)

# import time
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)











# Write a Python program to count the number of
#  even and odd numbers from a series of numbers.

# my_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11) 
# number_odd = 0
# number_even = 0
# for i in my_list:
#     if not i % 2==0:
#     	number_odd+=1
#     else:
#         number_even+=1
        
            
# print(number_even,number_odd)


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

# for i in range(7):
#     if i==3 or i==6:
#         continue
#     print(i)

# Write a Python program which accepts a sequence of comma separated 4 digit binary
#  numbers as its input and print the numbers that are divisible by 5 in a comma
#   separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010


# my_numbers = (input("Enter a number: "))
# my_list = my_numbers.split(",")
# for i in my_list:
#     j = int(i)
#     if j%5==0:
#         print(j)


# Write a Python program to check the validity of password input by users. 
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

















































































































        
    
        
    
































       





    























   





















































