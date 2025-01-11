t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a==b:
        print(c)
    elif a==c:
        print(b)
    else:
        print(a)