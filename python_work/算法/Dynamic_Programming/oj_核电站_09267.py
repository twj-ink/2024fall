'''dp
核电站 http://cs101.openjudge.cn/practice/09267
'''
n,m=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    if i<m:
        dp[i]=2**i
    elif i==m:
        dp[i]=2**i-1
    else:
        dp[i]=2*dp[i-1]-dp[i-1-m]
print(dp[-1])