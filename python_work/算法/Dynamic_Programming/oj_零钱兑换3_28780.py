'''dp 完全背包
零钱兑换3 http://cs101.openjudge.cn/practice/28780/
'''

n,m=map(int,input().split())
coins=[0]+list(map(int,input().split()))
dp=[0]+[float('inf')]*m
for i in range(1,n+1):
    for j in range(coins[i],m+1):
        dp[j]=min(dp[j],dp[j-coins[i]]+1)
print(dp[-1] if dp[-1]!=float('inf') else -1)
