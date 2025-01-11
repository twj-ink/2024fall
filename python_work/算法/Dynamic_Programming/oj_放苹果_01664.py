#复杂的整数划分-分成若干组
#dp[n][k]---把n分成k组
def divide(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    #所有整数分成1组都是1种
    for i in range(n+1):
        dp[i][1]=1
    for i in range(1,n+1):
        for j in range(1,k+1):
            #i<j时是不可能的
            if i>=j:
#当分割后有1时，把1拿出来单独一组，剩下的i-1分成j-1组
#当分割后无1时，从j中拿出来i，分到i组里，每组分1；然后剩下i-j再分成i组
                dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
    return sum(dp[n][i] for i in range(1,k+1))
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    print(divide(n,k))