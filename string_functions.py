name = "naina and tulsi"
name2 = " Cybersecurity7 "


print("Original string:", name)
print("-" * 51)

print("Length of string:", len(name))
print("Lowercase:", name.lower())
print("Uppercase:", name.upper())
print("Capitalized:", name.capitalize())
print("Title case:", name.title())
print("Swapped case:", name.swapcase())
print("Starts with 'nai':", name.startswith("nai"))
print("Ends with 'tulsi':", name.endswith("tulsi"))
print("Count of 'a':", name.count("a"))
print("First index of 'a':", name.find("a"))
print("Index of 'and':", name.index("and"))
print("Replacing 'naina' with 'tulsi':", name.replace("naina", "tulsi"))
print("Split by space:", name.split(" "))
print("Joined with hyphen:", "-".join(name.split(" ")))

print("Is name1 alphabetic only:", name.isalpha())
print("Is name2 alphabetic only:", name2.isalpha())
print("Is name1 alphanumeric:", name.isalnum())
print("Is name2 alphanumeric:", name2.isalnum())
print("Is digit:", name.isdigit())
print("Is name2 digit:", name2.isdigit())
print("Is lowercase:", name.islower())
print("Is name2 lowercase:", name2.islower())
print("Is uppercase:", name.isupper())
print("Is name2 uppercase:", name2.isupper())
print("Is whitespace only:", name.isspace())
print("Is name2 whitespace only:", name2.isspace())
print("Stripped (no spaces at start/end):", name.strip())
print("Stripped for the name2 (no spaces at start/end):", name2.strip())
print("Left stripped:", name.lstrip())
print("Right stripped:", name.rstrip())



