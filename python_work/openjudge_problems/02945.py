k=int(input())
a=list(map(int,input().split()))
dp=[1]*k
for i in range(1,len(a)):
    for j in range(0,i):
        if a[j]>=a[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))