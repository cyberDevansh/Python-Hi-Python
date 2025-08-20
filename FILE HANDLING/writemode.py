p="\nthis is added from file writemode.py"
f=open("file4.txt", "r+")
f.seek(0)
print(f.read())
f.write(p)
f.seek(0)
print(f.read())
f.close()