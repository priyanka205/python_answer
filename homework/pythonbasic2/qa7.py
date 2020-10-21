# Arrange String characters such that lowercase letters should come first.
# Example:
# Input: "aeiNPTvy"
# Ouput: "yaivePNT"
my_list = "aeiNPTvy"
lower = []
upper = []
for i in my_list:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
    l = "".join(lower)
    u = " ".join(upper)
    final_string = l + u
    print(final_string)


