# ) Generate  random String of length 5

# Note: String must be the combination of the UPPER case and lower case letters only. 
# No numbers and a special symbol.

import random
import string
random_letters = random.choices(string.ascii_uppercase+string.ascii_lowercase, k=5)
final_string = "".join(random_letters)
print(final_string)