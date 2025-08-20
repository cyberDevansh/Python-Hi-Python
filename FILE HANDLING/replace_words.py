words=["shit", "dumb", "fucked"]
with open("file6.txt", "r") as f:
    content = f.read()

for word in words:
    content= content.replace(word,"*"*len(word))
with open("file6.txt","w") as f:
        f.write(content)