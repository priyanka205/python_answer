# 4)Given a string of odd length greater 7,
#  return a string made of the middle three chars of a given String.
# Example:
# getMiddleThreeChars("JhonDipPeta") → "Dip"
# getMiddleThreeChars("Jasonay") → "son"


def my_char(x):

   return x[(len(x)-2)//2:(len(x)+3)//2]

print(my_char("JhonDipPeta"))

print(my_char("Jasonay"))

