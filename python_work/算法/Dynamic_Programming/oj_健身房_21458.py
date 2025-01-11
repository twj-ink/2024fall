'''dp 01背包
健身房 http://cs101.openjudge.cn/2024fallroutine/21458/
找V n cost=[  ] price=[  ]
'''

T,n=map(int,input().split())
ts,ws=[0],[0]
for _ in range(n):
    t,w=map(int,input().split())
    ts.append(t)
    ws.append(w)

dp=[0]+[-float('inf')]*T
for i in range(1,n+1):
    for j in range(T,ts[i]-1,-1):
        dp[j]=max(dp[j],dp[j-ts[i]]+ws[i])

if dp[-1]!=-float('inf'):
    print(dp[-1])
else:
    print(-1)
