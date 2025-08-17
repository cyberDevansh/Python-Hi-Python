a="subscribe this"
b="click here"
c="link below"
d="buy now"

message=input("Enter Your Comment:")
if((a in message ) or b in message or c in message or d in message):
    print("Spam message.")
else:
    print("Clear comments recieved.")
    