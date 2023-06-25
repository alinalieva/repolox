import random
import string

def generate_random_password(length, include_digits=True, include_symbols=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_random_password(8))
print(generate_random_password(10, include_digits=False))
