#类似与完全背包，设置二维dp数组
#由于求的是方案数，所以dp[i][j]表示i数字有j划分的方案数
while True:
    try:
        # n=int(input())
        # dp=[[0]*(n+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[1][i]=1
        #     dp[i][0]=1
        # for i in range(2,n+1):
        #     for j in range(1,n+1):#不选i的时候可以用1补齐，所以一直有dp[i-1][j]
        #         dp[i][j]=dp[i-1][j]+(dp[i][j-i] if j-i>=0 else 0)
        # # for i in dp:
        # #     print(*i)
        # print(dp[-1][-1])
        n=int(input())
        dp=[1]+[0]*n
        for i in range(1,n+1):
            for j in range(i,n+1):
                dp[j]+=dp[j-i]
        print(dp[-1])
    except EOFError:
        break
