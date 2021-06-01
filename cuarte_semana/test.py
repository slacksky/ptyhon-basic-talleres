import random
import string

def get_random_alphanumeric_string(length):
    letters = string.ascii_letters 
    result_str = ''.join((random.choice(letters) for i in range(length)))
    print("Random alpha String is:", result_str.lower())

get_random_alphanumeric_string(8)
get_random_alphanumeric_string(8)