def f(n):
    a=b=1
    if n==1 or n==2:
        return b
    else:
        for _ in range(n-2):
            a,b=b,a+b
        return b

t=int(input())
for _ in range(t):
    n=int(input())
    print(f(n))