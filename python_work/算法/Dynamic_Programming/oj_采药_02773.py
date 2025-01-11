'''dp
采药 http://cs101.openjudge.cn/practice/02773
01背包问题
'''
t,m=map(int,input().split())
times,values=[0],[0]
for _ in range(m):
    a,b=map(int,input().split())
    times.append(a)
    values.append(b)

dp=[0]+[0]*t
for i in range(1,m+1):
    for j in range(t,times[i]-1,-1):
        dp[j]=max(dp[j],values[i]+dp[j-times[i]])
print(dp[-1])