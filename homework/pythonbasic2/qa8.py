#  Given a string input Count all lower case, upper case, digits, and special symbols.
# Example: 
# Input_str = "P@#yn26at^&i5ve"
# Total counts of chars, digits,and symbols Chars = 8 Digits = 3 Symbol = 4

input_str =  "P@#yn26at^&i5ve"

letter_count = 0

digit_count = 0
special_count = 0
for x in input_str:

    if x.islower() or x.isupper():
         letter_count+=1
    elif x.isnumeric():
        digit_count+=1
    else:
      special_count+=1
print(letter_count,digit_count,special_count)
  
     
      
 