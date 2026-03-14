import random
import string

# Function to generate password
def generate_password(length=12):
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all characters
    all_characters = lowercase + uppercase + digits + punctuation

    # Generate password
    password = ""
    for i in range(length):
        password += random.choice(all_characters)

    return password


# Generate a random password
new_password = generate_password()

print("Generated Password:", new_password)
