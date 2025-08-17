a=2
b="string"
c="two words"
d=float(a)
e=type(a)
print(a,b,c,d,e)
print(f"a={a}\nb={b}\nc={c}\nd={d}\ne={e}\n",a,b,c,d,e)
print(type(b))


name = "Alice"
print("Hello, {}!".format(name))

# With multiple variables
print("Name: {}, Age: {}".format("Gopal", 21))

# With indexed or named placeholders
print("Name: {0}, Age: {1}".format("Gopal", 21))
print("Name: {name}, Age: {age}".format(name="Gopal", age=21))


name = "Alice"
age = 21
print("Name: %s, Age: %d" % (name, age))
