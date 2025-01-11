'''dfs
迷宫可⾏路径数 简单 https://sunnywhy.com/sfbj/8/1/313
只有墙1 从左上到右下 路径数目
cnt->路径数目   到终点了continue到for循环
'''
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global cnt

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if maze[nx][ny]=='end':
            cnt+=1
            continue

        if maze[nx][ny]==0:
            maze[x][y]=1
            dfs(nx,ny)
            maze[x][y]=0

    return

n,m=map(int,input().split())
maze=[]
maze.append([-1 for _ in range(m+2)])
for _ in range(n):
    maze.append([-1]+[int(i) for i in input().split()]+[-1])
maze.append([-1 for _ in range(m+2)])

maze[1][1]='start'
maze[n][m]='end'

cnt=0
dfs(1,1)
print(cnt)