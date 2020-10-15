#  Reverse a given number and return true if it is the same as the original number.

# Example:
# number = 121
# Orignal and reverse number is equal
# True

#palindrome
number = 121
x = str(number)
rev = x[::-1]
rev_n = int(rev)
if number == rev_n:
    print("True")
else:
    print("False")



