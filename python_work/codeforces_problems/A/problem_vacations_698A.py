n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
if a[0]==0:
    dp[0]=1
i=1
while i<n:
    if a[i]==0:
        dp[i]=1
        i+=1
        continue
    if a[i]==a[i-1] and a[i]!=3:
        a[i]=100
        dp[i]=1
        i+=1
        continue
    if a[i]==3 and a[i-1]!=3:
        a[i]=3-a[i-1]
    i+=1

print(sum(dp))