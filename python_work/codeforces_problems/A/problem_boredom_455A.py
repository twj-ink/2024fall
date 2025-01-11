from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))
l=max(a)
d=defaultdict(int)
for i in a:
    d[i]+=1
dp=[0]*(l+1)
dp[0]=0
dp[1]=1*d[1]
for i in range(2,l+1):
    dp[i]=max(dp[i-2]+i*d[i],dp[i-1])
print(dp[-1])
