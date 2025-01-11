def binary():
    l,r=0,L//(n-m+1)
    while l<=r:
        mid=(l+r)//2
        if can_reach(mid):
            l=mid+1
        else:
            r=mid-1
    return r

def can_reach(mid):
    cnt=0
    curr=s[0]
    for i in range(1,n+2):
        if s[i]-curr>=mid:
            cnt+=1
            curr=s[i]
    return n+1>=cnt>=n-m+1

L,n,m=map(int,input().split())
s=[]
for _ in range(n):
    s.append(int(input()))
s=[0]+s+[L]
print(binary())
