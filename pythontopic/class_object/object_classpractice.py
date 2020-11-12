# Python class and object:
# Pytron is an object orinted programming language.
# almost everything in python is an object, with its proporties and methods.
# A class is like an object constructor, or a blueprint for creating objects.

# #######################################

# To create a class, use a keyword class:
# class Myclass:
#     x = 5
# p1 = Myclass()
# print(p1.x)


# function __init__():
# __init__(), its a built in function:
# All classes have a function called __init__, which is always executed when class is being initiated.
# Use the __init__() function to assign values to object properties, other opeartions that are necessary to do when 
# the object is being created.
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# Insert a function that prints a greeting, and execute it on the p1 object:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

# Note:
# The self parameter is a reference to the current instances of the class, 
# and is used to access variables that belong to the class classname(object):
# The self paramater  is a reference to the current instances of the class, and is used to access variables 
# that function in the class

# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name 
#         mysillyobject.age = age
#     def myfun(abc):
#          print("Hello my name is " + abc.name)

   

# p1 = Person("john", 36)
# p1.age = 40
# print(p1.age)

# Python Inheritance:
# Inhertance allows us to define a class that inhertis all the methods and properties from another class
# Parent class is the class being inherited from, also called base class
# child class is the class that inherits from another class, also called derived class.


# Create a parent class:
# Any class can be parent class, so the syntax is the same as creating any other class:

# Create a class named Person, with firstname and lastname properties, and a printname method:

# class Person:
#     def __init__(self, fname, lnam):
#         self.fname = fname
#         self.lname = lname 

# #     def printname(self):
#         print(self.fname, self.lname)

# x = Person("Priyanka", 30)
# x.printname()

# Create child class:

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname 
#         self.lname = lname 

#     def printname(self):
#         print(self.fname, self.lname)

# class Student(Person):
#     def __init__(self, fname, lname):
#        Person.__init__(self, fname, lname) 
        

# x = Student("Priyanka", 29)
# x.printname()






































