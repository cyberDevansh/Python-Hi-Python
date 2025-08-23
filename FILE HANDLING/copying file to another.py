with open("file8.txt" , "r") as f:
    p=f.read()
with open("file8_copy.txt" ,"w") as f:
    f.write(p)
