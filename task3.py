import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password has at least one of each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length
    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to make it random
    random.shuffle(password)

    return ''.join(password)

# User input
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))