#learnig how to use path:
# first change the drive if its in diffn drive eg: it its in f we want to change it to c, simply do :c
# too see what folder we have########## dir
# to go inside that folder################ cd
# class Myclass:
#     y = 5
# print(Myclass)
# class myclass():
#     x = 5
# print(myclass)
# class myclass():
#     x = 5
# p1 = myclass()
# print(p1.x)
# init(function)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
class Person:
  def __init__(self, name, age, lastname):
    self.name = name
    self.age = age
    self.lastname = lastname

  def myfunc(self):
    print("Hello my name is " + self.name, self.lastname)

p1 = Person("John", 36, "Shrestha")
p1.myfunc()

