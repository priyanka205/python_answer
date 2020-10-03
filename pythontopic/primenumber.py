
# # Prime number:

lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))
prime_numbers = []
for num in range(lower_limit,upper_limit+1):
    if num>1:#if we need to test with negative number
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            prime_numbers.append(num)

print(prime_numbers)

