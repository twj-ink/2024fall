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