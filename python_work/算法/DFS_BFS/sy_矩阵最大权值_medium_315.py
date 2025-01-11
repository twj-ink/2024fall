'''dfs
矩阵最⼤权值 中等 https://sunnywhy.com/sfbj/8/1/315
'''
max_v=-float('inf')
dx=[0,-1,1,0]
dy=[-1,0,0,1]

def dfs(x,y,now_v):
    global max_v
    if x==n and y==m:
        now_v+=maze[n][m]
        max_v=max(max_v,now_v)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]!=-200:
            curr=maze[x][y]
            maze[x][y]=-200
            dfs(nx,ny,now_v+curr)
            maze[x][y]=curr

n,m=map(int,input().split())
maze=[]
maze.append([-200 for _ in range(m+2)])
for _ in range(n):
    maze.append([-200]+[int(i) for i in input().split()]+[-200])
maze.append([-200 for _ in range(m+2)])

dfs(1,1,0)
print(max_v)
