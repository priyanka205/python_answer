# 22) Remove duplicate from a list and create a tuple and find the minimum and maximum number
# For Example:
# sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41

samplelist = [87,45,41,65,94,41,99,94] 
unique_elements = tuple(set(samplelist))
maximum = max(unique_elements)
minimum = min(unique_elements)
print(maximum, minimum)






 

