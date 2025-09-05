with (
    open("file01.txt", "r") as f1,
    open("file02.txt", "r") as f2
):
    data1 = f1.read()
    data2 = f2.read()

print("File01 contents:", data1)
print("File02 contents:", data2)
