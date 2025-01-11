t=int(input())
s=sorted(list(map(int,input().split())))
i,j=0,len(s)-1
ans=float('inf')
gap=float('inf')
while i<j:
    curr=s[i]+s[j]
    if curr==t:
        ans=curr
        break
    if abs(curr-t)<gap:
        gap=abs(curr-t)
        ans=curr
    if abs(curr-t)==gap:
        ans=min(curr,ans)
    if curr>t:
        j-=1
    else:
        i+=1
print(ans)
