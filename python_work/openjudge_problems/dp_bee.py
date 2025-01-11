n=int(input())
maxv=-1
values=[]
for _ in range(n):
    a,b=map(int,input().split())
    values.append(b-a+1)
    maxv=max(maxv,b-a+1)
dp=[0]*(maxv+1)
dp[0]=0
dp[1]=1
for i in range(2,maxv+1):
    dp[i]=dp[i-1]+dp[i-2]
for i in values:
    print(dp[i])