s = {1, 2, 2, 3}
print(s)  # {1, 2, 3}



s = {1, 2}
s.add(3)         # {1, 2, 3}
s.remove(2)      # {1, 3} → Error if element not present
print(s)
s.discard(5)     # Safe remove, no error if not found      
s.pop()          # Removes a random element
print(s)
s.clear()        # Empties the set
print(s)


a = {1, 2, 3}
b = {3, 4, 5}
c = b.copy()


print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric Difference → {1, 2, 4, 5}


print(1 in a)    # True
print(10 in a)   # False
len(a)  # number of elements

print(a.issubset(b))             #(all elements of a are in b or not)
print(b.issuperset(a))           # (b contains all elements of a or not)

x = {1, 2}
y = {3, 4}
print(x.isdisjoint(y))        # True (no common elements)

print(x.union(y))
print(x.intersection(y))
