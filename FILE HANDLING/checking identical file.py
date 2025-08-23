with open("file8.txt" , "r") as f:
    content1=f.read()
with open("file8_copy.txt" , "r") as f:
    content2=f.read()
if content1==content2:
    print("Yes file8.txt and file8_copy.txt are identical.")
else:
    print("Both files are different and not identical.")