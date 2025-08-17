a=bool(0)            # False
b=bool(0.0)          # False
c=bool("")           # False
d=bool([])           # False
e=bool(())           # False
f=bool({})           # False
g=bool(set())        # False
h=bool(None)         # False

print (f"a,b,c,d,e,f,g,h= {a,b,c,d,e,f,g,h}")