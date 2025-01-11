m=int(input())
n=int(input())
s=list(map(int,input().split()))
s = sorted(s, key=lambda x: str(x)*10, reverse=True)

# f=True
# for i in range(n-1):
#     f=False
#     for j in range(n-i-1):
#         if str(s[j])+str(s[j+1])<str(s[j+1])+str(s[j]):
#             s[j],s[j+1]=s[j+1],s[j]
#             f=True
#     if f==False:
#         break
for i in range(n-1,-1,-1):
    if len(str(s[i]))<=m:
        s=s[:i+1]
        break
# dp=[['']*(m+1) for _ in range(n)]
# for j in range(1,m+1):
#     if j>=len(str(s[0])):
#         dp[0][j]=str(s[0])
# for i in range(1,n):
#     for j in range(1,m+1):
#         if j-len(str(s[i]))>=0 and dp[i-1][j]:
#             dp[i][j]=str(max(int(dp[i-1][j]),int(dp[i-1][j-len(str(s[i]))]+str(s[i]))))
#         else:
#             dp[i][j]=dp[i-1][j]
# # for i in dp: print(*i)
# if dp[-1][-1]:
#     print(int(dp[-1][-1]))
# else:
#     print('')

dp=['']*(m+1)
for j in range(m+1):
    if j>=len(str(s[0])):
        dp[j]=str(s[0])
for i in range(1,n):
    for j in range(m,0,-1):
        if j-len(str(s[i]))>=0 and dp[j]:
            dp[j]=str(max(int(dp[j]),int(dp[j-int(len(str(s[i])))]+str(s[i]))))
if dp[-1]:
    print(int(dp[-1]))
else:
    print("")