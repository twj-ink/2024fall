n,m=map(int,input().split())
coins=list(map(int,input().split()))
dp=[0]+[float('inf')]*m
for i in range(1,m+1):
    for coin in coins:
        dp[i]=min(dp[i],dp[i-coin]+1)
print(dp[-1] if dp[-1]!=float('inf') else -1)