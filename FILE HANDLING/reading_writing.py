f=open("file1.txt", "r+")
print(f.read())
print(f.write("\nThis line is created by reading_writing.py file using python.\n"))
print(f.read())
f.close()


#read takes input in digit for number of character to read

#output is not correct in first case as it reads by cursor so after f.write the cursor is at end of file so when called f.read again it gives empty string.



f = open("file1.txt", "r+")
f.seek(0)
print(f.read())
f.write("Checking again\n")
f.seek(0)         # move cursor to start
print(f.read())   
f.close()
