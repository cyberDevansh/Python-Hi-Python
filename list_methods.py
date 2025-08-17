#these are called list methods 
words = ["cyber", "security", "network"]

print("Original List:", words)

# append() – Add a new word at the end
words.append("cybercrime")
print("After append:", words)   

# insert() – Insert at index 1
words.insert(1, "cyberspace")
print("After insert:", words)

# extend() – Add multiple items from another iterable
words.extend(["cyberbullying", "cybersecurity"])
print("After extend:", words)

# remove() – Remove first occurrence of a word
words.remove("cyber")
print("After remove:", words)

# pop() – Remove and return last item
last_item = words.pop()
print("After pop:", words)
print("Popped item:", last_item)

# index() – Find index of a word
idx = words.index("cyberspace")
print("Index of 'cyberspace':", idx)

# count() – Count how many times a word occurs
cyber_count = words.count("cybersecurity")
print("Count of 'cybersecurity':", cyber_count)

# sort() – Sort alphabetically
words.sort()
print("After sort:", words)

# reverse() – Reverse the list
words.reverse()
print("After reverse:", words)

# copy() – Copy the list
words_copy = words.copy()
print("Copied list:", words_copy)

# clear() – Empty the original list
words.clear()
print("After clear (original list):", words)
print("Copied list still exists:", words_copy)
