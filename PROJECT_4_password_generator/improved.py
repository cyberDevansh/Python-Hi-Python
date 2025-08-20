import random
import string

def generate_password(length, choice):
    if choice == "1":
        characters = string.ascii_letters  # only letters
    elif choice == "2":
        characters = string.ascii_letters + string.digits  # letters + numbers
    elif choice == "3":
        characters = string.ascii_letters + string.digits + string.punctuation  # strong
    else:
        return None
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password


while True:
    print("\n🔐 Password Generator Menu:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Strong (Letters + Numbers + Symbols)")
    print("Type 'exit' to quit")

    user_input = input("\nEnter your choice (1/2/3 or 'exit'): ")

    if user_input.lower() == "exit":
        print("Exiting password generator. Bye!")
        break

    if user_input in ["1", "2", "3"]:
        length_input = input("Enter password length: ")

        if length_input.isdigit():
            length = int(length_input)
            password = generate_password(length, user_input)
            print("👉 Your password is:", password)
        else:
            print("⚠️ Please enter a valid number for length.")
    else:
        print("⚠️ Invalid choice! Try again.")
