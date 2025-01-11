n,m=map(int,input().split())
*a,=map(int,input().split())
curr={a[-1]}
dp=[0]*(n-1)+[1]
for i in range(n-2,-1,-1):
    dp[i]=dp[i+1]+(0 if a[i] in curr else 1)
    curr.add(a[i])
for _ in range(m):
    t=int(input())
    print(dp[t-1])