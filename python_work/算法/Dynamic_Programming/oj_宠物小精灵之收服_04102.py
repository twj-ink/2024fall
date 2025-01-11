###二位费用的01背包###
n,m,k=map(int,input().split())
#精灵球数量，体力值，精灵数量
dp=[[0]*(m+1) for _ in range(n+1)]#收服的精灵数量
# for i in range(n+1):
#     dp[i][0]=0
# for j in range(m+1):
#     dp[0][j]=0
for i in range(k):
    cn,cd=map(int,input().split())
    for j in range(n,cn-1,-1):#每个精灵球容量
        for q in range(m,cd-1,-1):#每个体力值容量
            dp[j][q]=max(dp[j][q],1+dp[j-cn][q-cd])
x=dp[-1][-1]
k=m
while k>-1 and dp[n][k]==dp[n][m]:
    k-=1
print(x,m-k-1)
