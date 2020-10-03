#  Write a Python program to divide a path on the extension separator.

path = "java.com"
name = path.split(".")
required= name[0]
print(required)

# if there is more than  1 . we can use this method:

filename = "https://www.practice.com.py"
name = filename.split(".")
required = name[0:-1]
r = ".".join(required)
print(r)