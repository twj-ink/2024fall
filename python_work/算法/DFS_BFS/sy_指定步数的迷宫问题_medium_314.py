'''dfs
指定步数的迷宫问题 中等 https://sunnywhy.com/sfbj/8/1/314
只有墙1 问能否在第k步移到终点
到终点了continue到for循环
'''

dx=[0,-1,1,0]
dy=[-1,0,0,1]

can_reach=False
def dfs(x,y,step):
    global can_reach
    # if can_reach:
    #     return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]=='end':
            if step==k-1:
                can_reach=True
                return
            continue
        if maze[nx][ny]==0:
            if step<k-1:
                maze[x][y]=1
                dfs(nx,ny,step+1)
                maze[x][y]=0

n,m,k=map(int,input().split())
#set protection square
maze=[]
maze.append([-1 for _ in range(m+2)])
for _ in range(n):
    maze.append([-1]+[int(i) for i in input().split()]+[-1])
maze.append([-1 for _ in range(m+2)])

maze[n][m]='end'
dfs(1,1,0)
print('Yes' if can_reach else 'No')