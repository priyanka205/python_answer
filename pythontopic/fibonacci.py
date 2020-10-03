#  Fibonacci Numbers:
# n1,n2 = 1,2
count = 0
fib_limit = int(input("fibonacci series upto: "))
if fib_limit>0:#to check negative
    if fib_limit==1:
        print(n1)
    else:
        while count<fib_limit:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        
else:
    ("please enter posative number.")

# by using for loop:


n1,n2 = 1,2
fib_limit = int(input("fibonacci series upto: " ))
if fib_limit>0:
    if fib_limit==1:
        print(n1)
    else:
        for i in range(fib_limit):
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
else:
     print("please enter posative number.")

        



