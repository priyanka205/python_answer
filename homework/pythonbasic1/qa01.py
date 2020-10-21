#    1) Write a Python program to sum of two given integers. 
#    However, if the sum is between 15 to 20 it will return 20.

#  Please use return statement for both if and else.  


x = int(input("Input x :"))
y = int(input("Input y: "))
def z(x, y):
    z = x + y
    if z in range(15, 20):
        return 20
    else:
        return z

print(z(x, y))
    






    


   



