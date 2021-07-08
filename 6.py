a=int(input())
b=int(input())
def test_range(n):
    if n in range(a,b):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
c=int(input())
print(test_range(c))