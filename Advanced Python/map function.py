l= [1,2,3,4,5]
square=lambda x:x*x

squaredlist=map(square, l)
print("Location=",squaredlist)
print(list(squaredlist))
print(list(squaredlist))   #map objects are iterators — once you loop through them or convert to a list, they get exhausted (empty).
print(square, type(square), type(squaredlist))  

   



#    1. List / Set / Dict Comprehensions
# These are eager → they immediately evaluate everything and store results in memory.

# 2. Generator Comprehensions
# These are lazy → they don’t store results, only generate on demand (just like map, filter, zip).

# trick:
#    Square brackets [] / curly {} / dict {key: value} → Eager (results stored).
# Parentheses () → Lazy (results generated on demand).
