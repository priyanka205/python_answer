#  Palindrome:when we see from left and right side we could see the same letter or number.
# eg:racecar

 

#  when Palindrome in string:
s = "racecar"
rev = s[::-1]
if s == rev:
  print(f"{s} is palindrome.")
else:
  print(f"{s} is not palindrome.")


# We can use through input too:
s = input("lets check: ")
rev = s[::-1]
if s == rev:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not palindrome")

# palindrome in number or int: 
# first we need to change int to str 

n = int(input("Enter a number:"))
sn = str(n)
rev = sn[::-1]
rev_n = int(rev)
if n== rev_n:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not palindrome")















































    



























