#dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+sum(j)-sum(i-1))
def mergeStone(n,s):
    #初始化，求最小值
    dp=[[float('inf')]*n for _ in range(n)]
    #初始化，dp[i][i]=0
    for i in range(n):
        dp[i][i]=0
    #计算前缀和
    prefix=[s[0]]+[0]*(n-1)
    for i in range(1,n):
        prefix[i]=prefix[i-1]+s[i]
    #dp
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+prefix[j]-(prefix[i-1] if i>=1 else 0))
    return dp[0][n-1]

n=int(input())
s=list(map(int,input().split()))
print(mergeStone(n,s))