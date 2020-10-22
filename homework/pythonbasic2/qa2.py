#  Given a list of numbers. Iterate over all the numbers, 
#  divide all of them by 5 and save the answers (float value) in a list with ascending order.

def fizzbuzz(x):
    for i in range(x):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}=fizzbuzz")
        elif i % 3 == 0:
            print(f"{i}=fizz")
        elif i % 5 == 0:
            print(f"{i}=buzz")
        else:
            continue
fizzbuzz(25)
    
    

     