'''dp
最长公共子序列 http://cs101.openjudge.cn/2024fallroutine/02806
如果匹配，dp[i][j]=dp[i-1][j-1]+1
如果不匹配，dp[i][j]=max(dp[i-1][j],dp[i][j-1])
'''


while True:
    try:
        a,b=input().split()
        n,m=len(b),len(a)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if a[j-1]==b[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        print(dp[-1][-1])
    except EOFError:
        break
