import sys
from heapq import heappop,heappush
sys.setrecursionlimit(1 << 30)






# dx,dy=[0,-1,1,0],[-1,0,0,1]
# max_v=1
# def dfs(x,y,dp):
#     global max_v
#     if all(s[x+dx[i]][y+dy[i]]>=s[x][y] for i in range(4)):
#         dp[x][y]=1
#         return
#     for i in range(4):
#         nx,ny=x+dx[i],y+dy[i]
#         if dp[nx][ny]==-1 and s[nx][ny]<s[x][y]:
#             dfs(nx,ny,dp)
#         if dp[nx][ny]!=-1 and s[nx][ny]<s[x][y]:
#             dp[x][y]=max(dp[x][y],1+dp[nx][ny])
#             max_v=max(max_v,dp[x][y])
#
#
#
# n,m=map(int,input().split())
# s=[];protect=[99999]*(m+2)
# s.append(protect)
# for _ in range(n):
#     s.append([99999]+list(map(int,input().split()))+[99999])
# s.append(protect)
# # for i in s: print(*i)
# # s=[[int(i) for i in input().split()] for _ in range(n)]
# dp=[[-1]*(m+2) for _ in range(n+2)]
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         dfs(i,j,dp)
# print(max_v)
# # for i in dp: print(*i)
