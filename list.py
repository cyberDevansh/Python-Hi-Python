# List – Like arrays, but dynamic(means mutable means changeable at any instant)
my_list = [10, "hello", 3.14, True]

print(my_list) 

print(my_list[1])         # "hello"
my_list[1] = "world"      # Modify
print(my_list[1]) 
my_list.append("new")     # Add at end
print(my_list) 
del my_list[0]            # Delete element
print(my_list[0]) 
print(my_list) 


#sorting of the list 
num=[1,4,2,5,2,77,3,0]
num.sort()
print (num)
num.reverse()
print (num)



#  Features:
# Ordered

# Changeable (mutable)

# Allows duplicates