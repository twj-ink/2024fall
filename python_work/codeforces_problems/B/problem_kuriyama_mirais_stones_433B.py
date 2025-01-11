n=int(input())
vs=list(map(int,input().split()))
sorted_vs=sorted(vs.copy())
m=int(input())

dp=[0]*n
dp[0]=vs[0]
for i in range(1,n):
    dp[i]=dp[i-1]+vs[i]
sorted_dp=[0]*n
sorted_dp[0]=sorted_vs[0]
for i in range(1,n):
    sorted_dp[i]=sorted_dp[i-1]+sorted_vs[i]

for _ in range(m):
    type,l,r=map(int,input().split())

    if type==1:
        print((dp[r-1]-dp[l-2]) if l!=1 else dp[r-1])
    else:
        print((sorted_dp[r-1]-sorted_dp[l-2]) if l!=1 else sorted_dp[r-1])

