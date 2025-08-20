import random 

def game():
    print("You are playing the game...")
    score = random.randint(1, 1000)

    try:
        with open("highscore.txt", "r") as f:
            highscore = f.read()
            if highscore != "":
                highscore = int(highscore)
            else:
                highscore = 0
    except FileNotFoundError:   #If the file doesn’t exist, set highscore = 0.
        highscore = 0

    print(f"Your score: {score}")
    print(f"Highscore: {highscore}")

    if score > highscore:
        print(f"New Highscore!\n Highscore Now={score}")
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
