def get_next_permutation(a):
    n=len(a)
    k=-1
    for i in range(n-1,0,-1):
        if a[i-1]<a[i]:
            k=i-1
            break
    if k==-1:
        return a.reverse()
    l=-1
    for i in range(n-1,k,-1):
        if a[i]>a[k]:
            l=i
            break
    a[k],a[l]=a[l],a[k]
    a[k+1:]=reversed(a[k+1:])
    return a
input()
m=int(input())
a=list(map(int,input().split()))
if len(a)==1:
    print(*a)
else:
    for _ in range(m):
        a=get_next_permutation(a)
    print(*a)