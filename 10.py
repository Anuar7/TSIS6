def even(l):
    a = []
    for n in l:
        if n % 2 == 0:
            a.append(n)
    return a
s=list(map(int,input().split()))
print(even(s))