#reading file without storing in a variable f 
with open("file0.txt", "r") as f:
    print(f.read())   # auto closes

# open("data.txt", "r")  # file is opened but we cannot read/write

# If you don’t keep the reference in f, you cannot close it properly → leads to memory leaks.