
# 12) Given a string, return the sum and average of the digits that appear in the string, 
# ignoring all other characters
# For Example: –
# sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5
import re 
my_Str = "English = 78 Science = 83 Math = 68 History = 65"
my_list = [int(num) for num in re.findall(r'\b\d+\b', my_Str)]
fullmarks = 0
for mark in my_list:
  fullmarks+=mark

percentage = fullmarks/len(my_list)  
print( fullmarks, percentage)                                    