with open("file7.txt", "r") as f:
    content=f.read()
if "python" in content:
    print("python is present.")
else:
    print("Python is not present.")
    