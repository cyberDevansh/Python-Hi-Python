with open("file7.txt", "r") as f:
    lines = f.readlines()

lineno = 1
found = False
for line in lines:
    if "donkey" in line:
        print(f"donkey is present in file7.txt in line number {lineno}")
        found = True
    lineno += 1
if not found:
    print("No donkey is present in file7.txt")
