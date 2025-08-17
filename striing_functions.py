name = "naina" 
b="TULSI ji"
print (len(name))

print (name.endswith("ina")) # this checks and gives the boolean whether the string is ending with the given last letterss or not 

print (name.startswith("nai"))  

print(name.capitalize()) 

print(b.lower())
print(b.upper())

print("Split by space:", b.split(" "))
print("Joined with hyphen:", "_".join(b.split(" ")))