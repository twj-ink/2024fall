'''dp 多重背包
NBA门票 http://cs101.openjudge.cn/practice/20089/
将个数拆成1 2 4等，每一份都用01背包解决
由于钱都是50的倍数，内层逆向遍历采用-50为步长有效降低时间复杂度
'''

N=int(input())
cost=[0,50,100,250,500,1000,2500,5000]
s=[0]+list(map(int,input().split()))
dp=[0]+[float('inf')]*N
for i in range(1,8):
    k=1
    while s[i]>0:
        cnt=min(k,s[i])
        for j in range(N,cnt*cost[i]-1,-50):
            if 0<=j-cnt*cost[i]<=N:
                dp[j]=min(dp[j],cnt+dp[j-cnt*cost[i]])
        s[i]-=cnt
        k*=2
if dp[-1]!=float('inf'):
    print(dp[-1])
else:
    print('Fail')
