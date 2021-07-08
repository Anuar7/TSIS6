def max(a,b,c): 
    if a >= b and a >= c:
        mx = a
    elif b >= a and b >= c:
        mx = b
    else:
        mx = c      
    return mx
a,b,c = map(int,input().split())
print(max(a,b,c))