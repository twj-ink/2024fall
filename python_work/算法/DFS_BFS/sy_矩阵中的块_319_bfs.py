'''bfs
矩阵中的块 https://sunnywhy.com/sfbj/8/2/319
'''
dx=[0,-1,1,0]
dy=[-1,0,0,1]

def dfs(x,y):
    s[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if s[nx][ny]==1:
                dfs(nx,ny)

n,m=map(int,input().split())
cnt=0
s=[[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if s[i][j]==1:
            dfs(i,j)
            cnt+=1
print(cnt)