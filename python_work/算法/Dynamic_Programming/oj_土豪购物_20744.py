s=list(map(int,input().split(',')))
#dp:取？不取？
#dp[i][0]表示到第i个时，有可能已经出现了不取的情况->该处不取？之前有可能已有不取的该处取？该处单独取比之间还大？
#dp[i][1]表示到第i个时，未出现不取的情况->接着取该处？该处单独取比之前的都大？
dp=[[0,0] for _ in range(len(s))]
dp[0][0]=s[0]
dp[0][1]=s[0]
for i in range(1,len(s)):
    dp[i][0]=max(dp[i-1][1],max(dp[i-1][0]+s[i],s[i]))
    dp[i][1]=max(dp[i-1][1]+s[i],s[i])
print(max(dp[i][0] for i in range(len(s))))