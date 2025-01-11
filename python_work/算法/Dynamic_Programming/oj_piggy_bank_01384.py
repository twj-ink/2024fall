'''dp 完全背包
Piggy-Bank http://cs101.openjudge.cn/practice/01384/
总容量V
物品n个，price=[     ] ; cost=[     ]
如果存在无解，初始化要设定为inf
dp=[0]+[-inf]*V
for i in range(1,n+1):     每个物品
    for j in range(weight[i],V+1):    能够装的容量
        dp[j]=max(dp[j],price[i]+dp[j-weight[i]])
                不装       装
return dp[-1] if dp[-1]!=-inf
'''
#该题特殊，求装满背包的最小价值，
#初始化为inf，每次取min而不是max
for _ in range(int(input())):
    e,f=map(int,input().split())

    V=f-e
    n=int(input())

    weight,price=[0],[0]
    for _ in range(n):
        p,w=map(int,input().split())
        weight.append(w)
        price.append(p)

    dp=[0]+[float('inf')]*V
    for i in range(1,n+1):
        for j in range(weight[i],V+1):
            dp[j]=min(dp[j],price[i]+dp[j-weight[i]])

    if dp[-1]==float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[-1]}.')