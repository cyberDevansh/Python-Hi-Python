# Using walrus to avoid recalculating
numbers = [5, 12, 7, 18, 3]

# Find and print numbers whose square is greater than 100
for n in numbers:
    if (sq := n * n) > 100:   # assign square inside condition
        print(f"{n} squared is {sq}, which is > 100")
