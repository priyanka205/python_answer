) Generate  random String of length 5

Note: String must be the combination of the UPPER case and lower case letters only. 
No numbers and a special symbol.

import random
import string

defint get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(8)
get_random_string(8)
get_random_string(6)