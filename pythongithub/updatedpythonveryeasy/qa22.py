# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. 




numbers = [2,15,19,25,60,45,38]
for x in numbers:
   if x % 15 == 0:
      print(x)
   else:
      print(x, "is not divisible")