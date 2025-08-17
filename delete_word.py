m = ["Gopalji", "Naina", "Bittu", "tu"]

def delete(sabd):
    n = []
    for item in m:
        if item != sabd:
            n.append(item.replace(sabd, ""))  # removes sabd from anywhere in the string
    return n

print(delete("tu"))
