#this will only check the firsst occurenceof the word in teh file
with open("file7.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "donkey" in line:
        print(f"donkey is present in file7.txt in line number {lineno}")
        break
    lineno += 1 
else:
    print("No donkey is present in file7.txt")
