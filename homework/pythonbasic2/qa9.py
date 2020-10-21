# ) Given two strings, s1 and s2, create a mixed String

# Note: create a third-string made of the first char of the last char of b,
# the second char of the second last char of b, and so on. Any leftover chars go at the
# end of the result.
# Input: "Pynative", "Website" 
# Expected Outcome: "PeytniastbievWe"

my_str1 =  "Pynative"
my_str2 = "Website" 
reserve_str2 = my_str2[::-1]
final_string = ""
if len(my_str1)>len(my_str2):
    for i, data in enumerate(my_str1):
        if i<len(reserve_str2):
            s = data+reserve_str2[i]
            final_string += data
else:
    for i, data in enumerate(reserve_str2):
        if i<len(my_str1):
            s = data+my_str[i]
        else:
            final_string +=data
print(final_string)
