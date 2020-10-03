#  Write a Python program to convert height (in feet and inches) to centimeters. 

x_ft = int(input("give ft:"))
y_in = int(input("give in:"))
x_cm = x_ft*30.48
y_cm = y_in*2.54
total_cm = x_cm + y_cm
print(total_cm)