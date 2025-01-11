def binary_search():
    l=0
    r=(s[-1]-s[0])//(c-1)
    while l<=r:
        mid=(l+r)//2
        if can_reach(mid):
            l=mid+1
        else:
            r=mid-1
    return r

def can_reach(mid):
    cnt=1
    curr=s[0]
    for i in range(1,n):
        if s[i]-curr>=mid:
            cnt+=1
            curr=s[i]
    return cnt>=c

n,c=map(int,input().split())
s=sorted([int(input()) for _ in range(n)])
print(binary_search())