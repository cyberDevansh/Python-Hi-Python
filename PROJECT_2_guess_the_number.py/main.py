import random

def guess_the_number():
    rounds = 3 
    
    for i in range(rounds):
        number = random.randint(1, 10) 
        print(f"\nRound {i+1}: Guess the number between 1 and 10")

        guess = int(input("Enter your guess: "))

        if guess == number:
            print("🎉 Correct! You guessed it right.")
        else:
            print(f"❌ Wrong! The number was {number}.")

   
    choice = input("\nDo you want to play again? (y/n): ")
    if choice.lower() == "y":
        guess_the_number()  
    else:
        print("Thanks for playing! 👋")


guess_the_number()
