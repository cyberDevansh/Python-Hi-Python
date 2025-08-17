# implementing program to detect double space in the string 
str= "I want to become a cybersecurity  expert  in the upcoming years."

print("Checking for double spaces in the string:\nAt index:", str.find("  "))

#only check the first occured double space not the all and if the output comes -1 then it means no double space is present in the given string

#now replacing the double space with the single one 
print(str.replace("  ", " "))
print(str)

# string is immutable means not changeable after once assigned so when we are printing by the replace function it is printing the new one string not changing the original string 