def sum(n):
    s=1
    for x in n:
        s*=x
    return s
a=map(int,input().split())
print(sum(a))