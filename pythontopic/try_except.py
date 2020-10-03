# try and except:
# these two comes together:

# Lets try with the example:

divider = [5,0,9,78,0,12]
num =5550
try:
    for i in divider:
        ans = num/i
        print(ans)
except:
    print("Something went wrong")

# we can put except  multiple times like else

divider = [5,6,9,78,0,12]
num =5550
try:
    for i in divider:
        ans = num/i
        print(ans)
except ZeroDivisionError:
    print("Number cannot be divide by zero.")
except:
    print("Spmething went wrong.")

#we can use here finally, finally:


divider = [5,6,9,78,0,12]
num =5550
try:
    for i in divider:
        ans = num/i
        print(ans)
except ZeroDivisionError:
    print("Number cannot be divide by zero.")
except:
    print("Spmething went wrong.")
finally:
    print("programming is completed")# this will print anyhow 


    












