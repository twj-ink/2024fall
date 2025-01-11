n=int(input())
h1=list(map(int,input().split()))
h2=list(map(int,input().split()))
#dp=[[h1[0],h2[0],0] for _ in range(n)]
#for i in range(1,n):
#    dp[i][0]=max(dp[i-1][1]+h1[i],max(dp[i-1][2]+h1[i],h1[i]))
#    dp[i][1]=max(dp[i-1][0]+h2[i],max(dp[i-1][2]+h2[i],h2[i]))
#    dp[i][2]=max(dp[i-1][0],dp[i-1][1])
#print(max(dp[-1][0],max(dp[-1][1],dp[-1][2])))
dp=[[h1[0],h2[0]] for _ in range(n)]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1]+h1[i])
    dp[i][1]=max(dp[i-1][1],dp[i-1][0]+h2[i])
print(max(dp[-1][0],dp[-1][1]))
