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


# num = [30,20,10,12,15,46,45]
# minimum = 100000000
# for i in num:
#     if minimum>i:
#         minimum=i
# print(minimum)

# how to get maxmium value:

# num = [10,12,15,46,45]
# maximum = 0
# for i in num:
#     if maximum<i:
#         maximum=i
# print(maximum)  

# Palindrome:when we see from left and right side we could see the same letter or number.
# eg:racecar

 

# Palindrome in string:
# s = "racecar"
# rev = s[::-1]
# if s == rev:
#   print(f"{s} is palindrome.")
# else:
#   print(f"{s} is not palindrome.")


# We can use through input too:
# s = input("lets check: ")
# rev = s[::-1]
# if s == rev:
#     print(f"{s} is a palindrome")
# else:
#     print(f"{s} is not palindrome")

# palindrome in number or int: 
# first we need to change int to str 

# n = int(input("Enter a number:"))
# sn = str(n)
# rev = sn[::-1]
# rev_n = int(rev)
# if n== rev_n:
#     print(f"{n} is a palindrome")
# else:
#     print(f"{n} is not palindrome")


# # Prime number:

# lower_limit = int(input("Enter lower limit: "))
# upper_limit = int(input("Enter upper limit: "))
# prime_numbers = []
# for num in range(lower_limit,upper_limit+1):
#     if num>1:#if we need to test with negative number
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             prime_numbers.append(num)

# print(prime_numbers)

# Fibonacci Numbers:
# n1,n2 = 1,2
# count = 0
# fib_limit = int(input("fibonacci series upto: "))
# if fib_limit>0:#to check negative
#     if fib_limit==1:
#         print(n1)
#     else:
#         while count<fib_limit:
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count += 1
        
# else:
#     ("please enter posative number.")

#by using for loop:


# n1,n2 = 1,2
# fib_limit = int(input("fibonacci series upto: " ))
# if fib_limit>0:
#     if fib_limit==1:
#         print(n1)
#     else:
#         for i in range(fib_limit):
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
# else:
#      print("please enter posative number.")

        


















































    













































