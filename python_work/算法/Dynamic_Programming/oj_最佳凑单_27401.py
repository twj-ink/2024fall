#01背包
n,t=map(int,input().split())
s=list(map(int,input().split()))
a=sum(s)
if a<t:
    print(0)
elif a==t:
    print(t)
else:
    dp=[0]+[-float('inf')]*a
    for i in range(n):
        for j in range(a,s[i]-1,-1):
            dp[j]=max(dp[j],s[i]+dp[j-s[i]])
    for i in range(t,a+1):
        if dp[i]!=-float('inf'):
            print(i)
            break