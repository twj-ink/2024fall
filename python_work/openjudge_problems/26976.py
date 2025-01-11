n=int(input())
s=list(map(int,input().split()))
dp=[[0]*n for _ in range(2)]
dp[0][0]=dp[1][0]=1
for i in range(1,n):
    if s[i]>s[i-1]:
        dp[0][i]=max(dp[1][j] for j in range(0,i))+1
        dp[1][i]=dp[1][i-1]
    elif s[i]<s[i-1]:
        dp[1][i]=max(dp[0][j] for j in range(0,i))+1
        dp[0][i]=dp[0][i-1]
    else:
        dp[1][i]=dp[1][i-1]
        dp[0][i]=dp[0][i-1]
print(max(dp[0][-1],dp[1][-1]))