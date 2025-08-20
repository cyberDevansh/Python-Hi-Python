with open("file0.txt", "r") as f:
    print(f.read())
    f.seek(0)
    print(f.readline())
    f.seek(2)
    print(f.readlines())
    f.close