
# 6) Given 2 strings, s1, and s2 return a new string made of the first,
#  middle and last char each input string.

# Example:
# Input: "America", "Japan"
# Ouput: "AJrpan"

s1 = "America"
s2 = "Japan"
mix_str = []
x = s1[3]

y= s2[2] 

mix_str = s1[0] + s2[0] + x + y+ s1[-1] + s2[-1]

print(mix_str)
