import random
# game of the truth and dare for you

truth=["Do you have any crush in school", "Do you speak lie about your studies" , "What’s one thing you’ve done that you would never tell your parents?","What’s the weirdest thing you’ve searched for online?" , "What’s your most useless talent?" , "Have you ever pretended to like a gift you actually hated?"]

dare=["Text the first person in your contacts “I have a secret” and don’t reply for 10 minutes." , "Wear socks on your hands until the next round." , "Wear socks on your hands until the next round." , "Sing everything you say for the next 5 minutes."]

plyr_choose=input("What you want to choose:Truth or Dare?\nInput:").lower()

if plyr_choose not in ["truth" , "dare"]:
    print("Wrong INput!")
else:
    if plyr_choose=="truth":
        print(random.choice(truth))
    
    elif plyr_choose=="dare":
        print(random.choice(dare))

    else:
        print("Something went wrong.")