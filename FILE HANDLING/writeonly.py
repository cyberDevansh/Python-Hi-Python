with open("file2.txt" , "w") as f:
    f.write("This is created using writeonly.py file.")
    f.close()



#noraml methodds

g=open("file2.txt", "r")
print(g.read())
g.close()



#Python nukes whatever was inside and starts fresh. That’s why your second open("file2.txt", "w") erased the first line and left only:THis is again checking.
