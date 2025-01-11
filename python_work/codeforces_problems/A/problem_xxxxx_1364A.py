t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    l,r=0,n-1
    if sum(a)%x!=0:
        print(n)
    else:
        while a[l]%x==0 and l<n-1:
            l+=1
        while a[r]%x==0 and r>0:
            r-=1
        if l<=r:
            m=min(l,n-1-r)
            print(n-m-1 if n-m-1 else -1)
        else:
            print(-1)
