# replacing a word and printing in which line it got replaced.
words = ["shit", "dumb", "fucked"]

with open("file6.txt", "r") as f:
    lines = f.readlines()   # read file line by line

for i, line in enumerate(lines, start=1):  
    original_line = line
    for word in words:
        if word in line:   
            print(f"Word '{word}' replaced in line {i}")
            line = line.replace(word, "*" * len(word))  
    lines[i-1] = line 

with open("file6.txt", "w") as f:
    f.writelines(lines)
