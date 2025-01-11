'''dp
最大上升子序列和 http://cs101.openjudge.cn/practice/solution/46828902/
与拦截导弹、最大上升子序列不同的是，该题dp初始不是1而是每个数字本身
且dp[i]=max(dp[i],dp[j]+s[i])
'''

k=int(input())
a=list(map(int,input().split()))
dp=[0]*k
for i in range(len(a)):
    dp[i]=a[i]
for i in range(1,len(a)):
    for j in range(0,i):
        if a[j]<a[i]:
            dp[i]=max(dp[i],dp[j]+a[i])

print(max(dp))