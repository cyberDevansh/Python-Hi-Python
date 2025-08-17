def pattern(n):
    if(n==0):
        return
    else:
        print("*" * n)
        # return pattern(n-1)
        pattern(n-1)    #also i can write return pattern n-1

pattern(5)