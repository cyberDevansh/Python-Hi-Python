import random

def play_round():
    choices = ["stone", "paper", "scissors"] 
    try:
        userchoice = input("Enter your choice (Stone, Paper, Scissors): ").lower()
        
        if userchoice not in choices:
            print("You miss-typed or broke the rule! Try again.")
            return None

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice.capitalize())

        # checking for the winner
        if userchoice == computer_choice:
            print("It's a tie!")
        elif (userchoice == "stone" and computer_choice == "scissors") or (userchoice == "paper" and computer_choice == "stone") or (userchoice == "scissors" and computer_choice == "paper"):
            print("✅ You win!")
        else:
            print(" You lost to the computer.")
    
    except Exception:
        print("Something went wrong!")

while True:
    print("\n--- Let's play 3 rounds ---")
    for _ in range(3):
        play_round()
        print("-" * 108)
    
    more = input("Do you want to play 3 more rounds? (y/n): ").lower()
    if more != "y":
        print("Thanks for playing! 👋")
        break
