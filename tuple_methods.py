t = (10, 20, 50, 30, 10)

#count
print(t.count(10))   
print(t.index(30))   
# print(t.index(99))  # ValueError

#indexing 
print(t[0])    
print(t[-1])   

#count and index are the main methods of tuple

# slicing
print(t[1:])   
print(t[:2])   

#length 
len(t) 

#looping 
for val in t:
    print(val)

#unpacking 
x, y, z = (1, 2, 3)
print(x, y, z)

#concatenation 
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  

#multiplication  
t4 = (1, 2) 
print(t4 * 3)  

#check if item exists or not in the tuple
print(20 in t)
print(25 in t)

x, _, z = (1, 2, 3)  
print(x,_,z)

x, *y = (1, 2, 3, 4)
print(x)   # 1
print(y)   # [2, 3, 4]
