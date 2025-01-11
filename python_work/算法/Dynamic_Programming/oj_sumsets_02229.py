'''dp 完全背包 但不是求最优解而是求所有解的个数
Sumsets http://cs101.openjudge.cn/routine/02229/
典型的dp[i]指在容量为i时的最大价值
这道题dp[i]指在和为i时的方案数(求的就是方案数)
'''
mod=10**9
n=int(input())
s=[2**i for i in range(21)]
dp=[1]+[0]*n
for i in range(21):
    for j in range(s[i],n+1):
        dp[j]+=dp[j-s[i]]%mod

print(dp[-1]%mod)
