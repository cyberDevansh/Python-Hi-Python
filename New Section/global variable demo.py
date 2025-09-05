a=10
def own():
    a=11
    print(a)



def second():
    global a
    print(a)



own()
print(a)
second()



def third():
    global a
    a=5
    print(a)


third()
print(a)