t=int(input())
for _ in range(t):
    x,y,n=map(int,input().split())
    if n%x>=y:
        m=n-(n%x-y)
        print(int(m))
    else:
        m=n-(n%x+x-y)
        print(int(m))