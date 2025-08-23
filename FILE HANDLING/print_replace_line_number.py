# replacing a word and printing in which line it got replaced.
words = ["shit", "dumb", "fucked"]
with open("file7.txt", "r") as f:
    lines = f.readlines() # read each line as list

for i in range(len(lines)):  
    for word in words:  
        if word in lines[i]: 
            print(f"Word '{word}' replaced in line {i+1}")
            lines[i] = lines[i].replace(word, "*" * len(word))

with open("file7.txt", "w") as f:
    f.writelines(lines)
 