# 22) Remove duplicate from a list and create a tuple and find the minimum and maximum number
# For Example:
# sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41

samplelist = [87,45,41,65,94,41,99,94] 
non_duplicate = []
duplicate = []
for i in samplelist:
    current_num = samplelist.pop(0)
    if current_num in samplelist:
        duplicate.append(i)
        samplelist.remove(current_num)
    else:
        non_duplicate.append(current_num)


print(non_duplicate)
print(duplicate)




# sampleList = list(set(samplelist))
# print("unique list", samplelist)

# tuple = tuple(samplelist)
# print("tuple ", tuple)

# print("Minimum number is: ", min(tuple))


 

