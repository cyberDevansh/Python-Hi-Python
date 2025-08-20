import random
import string

def generate_password(length):
    # All possible characters (letters + digits + symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

while True:
    user_input = input("Enter password length (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting password generator. Bye!")
        break

    if user_input.isdigit():  # check if user entered a number
        length = int(user_input)
        print("Your random password is:", generate_password(length))
    else:
        print("⚠️ Please enter a valid number or 'exit'.")
