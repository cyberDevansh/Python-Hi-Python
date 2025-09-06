# list comprehension = one-liner for loops with optional conditions.


#normal way 
squares = []
for i in range(5):
    squares.append(i * i)
print(squares)  




# With list comprehension

numbers = [i * i for i in range(5)]
print(numbers)  



#Adding condition (if filter)

evens = [i for i in range(10) if i % 2 == 0]
print(evens) 


# Nested loops inside comprehension

pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print(pairs)  
# this code is equivalant to 
# pairs = []
# for x in [1, 2, 3]:
#     for y in [4, 5, 6]:
#         pairs.append((x, y))
# print(pairs)



#If–else inside comprehension

labels = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
