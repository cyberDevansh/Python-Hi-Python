l = ["Gopalji", "Naina", "Bittu", "tu"]

def remove(word):
    if word in l:
        l.remove(word)
    return l

print(remove("tu")) # but this will not remove the in between letters in the words and only removes hte each alphabet writtern not as word but as letters
print(l)




m = ["Gopalji", "Naina", "Bittu", "tu"]

def delete(sabd): 
    n=[]
    for item in m:
        if not (item == sabd):
            n.append(item.strip(sabd))
    return n


print(delete("tu"))
print(m)