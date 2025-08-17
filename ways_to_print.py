a='name1'
b="name2"
c=2.5
d=int(c)
e=type(a)

print(a,b,c,d,e) #way1

print(f"a={a}\tb={b}\tc={c}\td={d}\te={e}\n")  #way2

print("a=",a,"b=",b,"c=",c)  # way 3

print("a="+(a)+"\tb="+ b+ "c="+str(c))  #way 4

print("a={}".format(a))   #way 5

print("a:{} b:{} c:{} d:{}".format(a,b,c,d))    #way 5

print("Name: {}, Age: {}".format("Gopal", 21))     #way 5

print("Name: {0}, Age: {1}".format("Gopal", 21))    #way 5

print("Name: {name}, Age: {age}".format(name="Gopal", age=21))    #way 5

print("a=%s b=%s c=%d d=%d" %(a,b,c,d))  #way 6

#way 7  Using repr() or str() explicitly
data = {'key': 10}
print("Data: " + repr(data))



#way8
import json
data = {'name': 'Alice', 'age': 21}
print(json.dumps(data, indent=2))



#way9
import pprint
data = {'name': 'Alice', 'skills': ['Python', 'C++', 'Linux']}
pprint.pprint(data)