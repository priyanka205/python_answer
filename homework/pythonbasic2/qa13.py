# 12) Given a string, return the sum and average of the digits that appear 
# in the string, ignoring all other characters
# For Example: –
# sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5


s = "English = 78 Science = 83 Math = 68 History = 65"
elements = s.split(" ")
numbers = []
for ele in elements:
    if ele.isdigit():
        numbers.append(int(ele))
total = sum(numbers)
ave = total/len(numbers)
print(f"Total of the numbers is {total} and average is {ave}.")


