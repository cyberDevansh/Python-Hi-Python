import random

highscore = None

def numbers():
    global highscore
    userscore = random.randint(1, 1000)
    userinput = input("Type 'play' to generate a number: ").lower()
    
    if userinput != "play":
        print("I think you mistyped.")
        return
    
    print(f"Highest Score: {highscore}")
    print(f"Your Score: {userscore}")
    
    if highscore is None or userscore > highscore:
        highscore = userscore
        print(f"Highscore Now: {highscore}")

while True:
    numbers()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! Goodbye!")
        break
