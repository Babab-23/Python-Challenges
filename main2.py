import random
import string

def generate_password(length):
    # Define the characters to choose from
    all_characters = string.ascii_letters + string.digits  # Uppercase, lowercase, and digits
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    # Shuffle the password for additional randomness
    password_list = list(password)
    random.shuffle(password_list)
    
    # Join the shuffled list back into a string
    return ''.join(password_list)

# Example usage:
password_length = 12  # Length of the password you want
password = generate_password(password_length)
print(f"Generated password: {password}")
