def un(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
b=list(map(int,input().split()))
print(un(b))