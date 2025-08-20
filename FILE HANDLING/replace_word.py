word="donkey"
with open("file5.txt", "r") as f:
    content = f.read()
content= content.replace(word,"###key")
with open("file5.txt", "w") as f:
    f.write(content)