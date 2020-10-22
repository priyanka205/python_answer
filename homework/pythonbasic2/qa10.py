# 10) String characters balance Test
# We’ll say that a String s1 and s2 is balanced if all the chars in the string1 are there in s2.
#  characters position doesn’t matter.
# For Example: –
# stringBalanceCheck(yn, Pynative) = True


def stringcheck(s1, s2):
  x = True
  for char in s1:
    if char in s2:
      continue
    else:
      x = False
  return x
  
s1 = "Yn"
s2 = "PYnative"
x = stringcheck(s1, s2)
print( x)

s1 = "Ynf"
s2 = "PYnative"
x = stringcheck(s1, s2)
print(x)



