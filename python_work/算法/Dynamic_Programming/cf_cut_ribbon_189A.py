'''dp 完全背包
Cut Ribbon https://codeforces.com/problemset/problem/189/A
'''

inf=-float('inf')
#每段的价值是1，代价占据的空间是本身a,b,c,总空间是n
a=list(map(int,input().split()))
n=a[0]
dp=[0]+[inf]*n
#对每个物品总遍历，对每一个能够装下的容量列遍历
for i in range(1,4):
    for j in range(a[i],n+1):
        dp[j]=max(dp[j],1+dp[j-a[i]])
print(dp[-1])