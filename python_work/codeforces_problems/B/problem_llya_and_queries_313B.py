s=input()
n=len(s)
m=int(input())

dp=[0]*n
for i in range(1,n):
    if s[i]==s[i-1]:
        dp[i]=dp[i-1]+1
    else:
        dp[i]=dp[i-1]

for _ in range(m):
    l,r=map(int,input().split())
    print(dp[r-1]-dp[l-1])