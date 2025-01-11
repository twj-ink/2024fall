'''dfs
矩阵最⼤权值路径 中等 https://sunnywhy.com/sfbj/8/1/316
'''
max_v=-float('inf')
max_path=[]
dx,dy=[0,-1,1,0],[-1,0,0,1]
def dfs(x,y,now_v,now_path):
    global max_v,max_path
    if x==n and y==m:
        now_v+=maze[n][m]
        now_path.append((n,m))
        if now_v>=max_v:
            max_v=now_v
            max_path=now_path[:]
        now_path.pop()
        return

    now_path.append((x,y))
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if maze[nx][ny]!=-200:
            curr=maze[x][y]
            maze[x][y]=-200
            dfs(nx,ny,now_v+curr,now_path)
            maze[x][y]=curr
    now_path.pop()

n,m=map(int,input().split())
maze=[[-200]*(m+2)]+[[-200]+list(map(int,input().split()))+[-200] for _ in range(n)]+[[-200]*(m+2)]
dfs(1,1,0,[])
for i in max_path:
    print(*i)