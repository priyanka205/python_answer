# 5) Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.

# Example:

# Input: "Chrisdem", amNewStringI

# Output: "ChrIamNewStringisdem"

s1 = "Chrisdem"
s2 = "IamNewStringI"
news2 = s1[:3] + s2 + s1[3:]

print(news2)
