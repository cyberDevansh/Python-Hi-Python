f=open("file0.txt" , "r")
line1=f.readline()
line2=f.readline()
line3=f.readline()


print(line1,line2,line3) # this is printinng little messy as \n is present in each line and print is also adding another \n so it is looking messy 
#output is this 
# Jai Siya Ram
#  Jai Sree Krishna
#  Namo Parvati Pataye, Har Har Mahadev
print(line1.strip(), line2.strip(), line3.strip()) #so this will remove the spaces 

#output is this 
# Jai Siya Ram Jai Sree Krishna Namo Parvati Pataye, Har Har Mahadev

print(line1, end="")  
print(line2, end="")  
print(line3, end="")
#end="" works on whole print not on individual items so we can not use all three lines in one liner
f.close()
