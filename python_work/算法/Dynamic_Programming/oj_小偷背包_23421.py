'''dp 01背包问题
背包总容量V
物品n个，cost=[             ] ; price=[            ]
dp=[0]*(V+1),表示每个容量所装的价值
for i in range(1,n+1):        每个物品
    for j in range(V,cost[i]-1,-1):       能装这个物品的空间
        dp[j]=max(dp[j],price[i]+dp[j-cost[i]])
                  不装   装
return dp[-1]
'''



n,b=map(int,input().split())
v=list(map(int,input().split()))
w=list(map(int,input().split()))
goods=[]
for i in range(n):
    goods.append((v[i],w[i]))
dp=[[0]*b for _ in range(n)]
for i in range(n):
    for j in range(b):
        if i==0 and goods[0][1]<=j+1:
            dp[0][j]=max(dp[0][j],goods[0][0])
        else:
            if goods[i][1]<=j+1:
                dp[i][j]=max(dp[i-1][j], goods[i][0]+(dp[i-1][j-goods[i][1]] if j-goods[i][1]>=0 else 0))
            else:
                dp[i][j]=dp[i-1][j]
#print(dp)
print(dp[-1][-1])



n,V=map(int,input().split())
price=[0]+[int(_) for _ in input().split()]
cost=[0]+[int(_) for _ in input().split()]
dp=[0]*(V+1)
for i in range(1,n+1):
    for c in range(V,cost[i]-1,-1):
        dp[c]=max(dp[c],price[i]+dp[c-cost[i]])
        if i==n:
            break
print(dp[-1])
