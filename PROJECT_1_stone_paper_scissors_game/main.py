import random 

def play_round():
    choices=["stone", "paper" , "scissors"]
    userchoice= input("🤞😁\nEnter your choice: Stone, Paper, Scissors\n").lower()
    if userchoice not in choices:
        print("INvalid choice! Either spelling mistake. Try again.")
        return None
    
    computer_choice= random.choice(choices)
    print("I choose:", computer_choice)

    # checking for the winner 

    if userchoice == computer_choice:
        print("Its tie!")
    elif( userchoice =='stone' and computer_choice=="scissors") or \
        (userchoice == "paper" and computer_choice =="stone") or \
        (userchoice=="scissors" and computer_choice== "paper"):
        print("You win!😎😅")
    else:
        print("You lost to me.😅😘")

while True:
    print("\n---Lets play 3 rounds" ,end="")
    for _ in range(3):
        play_round()
        print("-"*51)
    
    more =input("DO u wnat to play 3 more rounds? (y/n):").lower()
    if more!="y":
        print("Thanks for playing!")
        break