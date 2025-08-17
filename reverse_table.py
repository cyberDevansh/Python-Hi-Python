# printing table orderly and reversely 
n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}*{i}= {n*i}")
    
for j in range(1,11):
    print(f"\t{n}*{11-j}= {n*(11-j)}")
    