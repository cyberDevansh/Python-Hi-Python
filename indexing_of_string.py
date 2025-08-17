name = "naina"
name2= "tulsi gupta"
a= name[0:4]
b= name2[2:8]
print("a will store: {} (from index number 0 to 3)\nb will store: {} (from index number 2 to 7)".format(a,b))  

# using the negative indexing for the string 
c= name2[-9:-1]     #for this to calculate what will be printed we should start the indexing from the last character of the string from -1 to -infinity (according to the numbers given) and hence the output is known or try to convert it into the positive indexing and then find the output like in this case the corresponding positive indexes are c=name2[2,10] 

d= name2[2:10]
print (f"c will store:{c}")
print (f"d(it is same as c but the output by positive indexing) will store:{d}")

e=name2[:7]  # this is same as e=name2[0:7]
f= name2[3:]    # this means from 3 to last index
print(f"e={e}\nf={f}")