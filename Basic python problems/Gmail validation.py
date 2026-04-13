import re

def is_valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(pattern, email, re.IGNORECASE))

# Get email input from the user
user_email = input("Enter an email address to validate: ")

# Validate and print result
if is_valid_gmail(user_email):
    print(f"{user_email} is a valid Gmail address.")
else:
    print(f"{user_email} is NOT a valid Gmail address.")
