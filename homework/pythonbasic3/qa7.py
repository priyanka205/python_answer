# Write a function that prints all the prime numbers between 0 and
#  limit where limit is a parameter.


def my_prime(my_fun):
    if (my_fun > 1):
        for my_prime1 in range(2, my_fun+1):
            for my_prime2 in range(2, my_prime1):
 
                if (my_prime1 != 2 and my_prime1 % my_prime2 == 0):
                    break
            else:
                print(my_prime1)
 
print(my_prime(14))