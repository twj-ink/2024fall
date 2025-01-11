'''dp 完全背包
简单的整数划分问题 http://cs101.openjudge.cn/2024fallroutine/04117
'''
while True:
    try:
        n=int(input())
        dp=[1]+[0]*n
        for i in range(1,n+1):
            for j in range(i,n+1):
                dp[j]+=dp[j-i]
        print(dp[-1])
    except EOFError:
        break
