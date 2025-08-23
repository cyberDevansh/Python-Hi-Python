import os
with open("file00.txt", "r") as f:
    content = f.read()
with open("file10.txt", "w") as f:
    f.write(content)
os.remove("file00.txt")

print("File copied to file10.txt and old file00.txt deleted successfully.")
