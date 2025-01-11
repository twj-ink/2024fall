t=int(input())
for _ in range(t):
    l,n=map(int,input().split())
    s=sorted(list(map(int,input().split())))
    a=s[0]
    b=l-s[0]
    for i in s:
        a=max(a,min(i,l-i))
        b=max(b,max(i,l-i))
    print(a,b)