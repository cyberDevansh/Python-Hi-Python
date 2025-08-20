import random

computer=random.choice([1,0,-1])
userchoice= input("Enter your choice: Snake,Water,Gun:").lower()
youdict={
    "snake":1,
    "water":-1,
    "gun":0
   }
reversedict={
    1:"snake",
    0:"gun",
    -1:"water"
}
userchoosed=youdict[userchoice]   #here i stored the user choice in uesrchoosed in number for comparing 

print(f"YOu choosed:{userchoice}\n Computer choosed:{reversedict[computer]}")

if computer==userchoosed:
    print("Game Tied.")
else:
    if computer==1 and userchoosed==-1:
        print("YOu lost.")
    elif computer==1 and userchoosed==0:
        print("YOu won.")
    elif computer==0 and userchoosed==-1:
        print("YOu won.")
    elif computer==0 and userchoosed==1:
        print("YOu lost.")
    elif computer==-1 and userchoosed==0:
        print("YOu lost.")
    elif computer==-1 and userchoosed==1:
        print("YOu won.")
    else:
        print("Something went wrong.")





        # this can be easily done using little calcutlation 
#         result = computer - userchoosed
# if result == 0:
#     print("Game Tied.")
# elif result in [(1 - -1), (0 - 1), (-1 - 0)]:  # winning differences
#     print("You lost.")
# else:
#     print("You won.")
