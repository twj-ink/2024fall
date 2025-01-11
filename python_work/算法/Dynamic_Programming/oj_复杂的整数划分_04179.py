#N划分成K个正整数之和的划分数目
#dp[i][j]表示把i分成j个
def q1(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    #划分成自己1个
    for i in range(n+1):
        dp[i][1]=1
    for i in range(1,n+1):
        for j in range(1,k+1):
            if i>=j:
                #划分包含1，为dp[i-1][j-1]
                #不包含1，拿出来j个放到j组里面，为dp[i-j][j]
                dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
    return dp[-1][-1]
#N划分成若干个不同正整数之和的划分数目  01背包
def q2(n):
    dp=[1]+[0]*n
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            dp[j]+=dp[j-i]
    return dp[-1]

def q3(n):
    dp=[1]+[0]*n
    for i in range(1,n+1,2):
        for j in range(i,n+1):
            dp[j]+=dp[j-i]
    return dp[-1]
while True:
    try:
        n,k=map(int,input().split())
        print(q1(n,k))
        print(q2(n))
        print(q3(n))
    except EOFError:
        break