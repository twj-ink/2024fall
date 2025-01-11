#设置一个每个位置为(-1,-1)的二维坐标，每个位置更新为到达这个位置的迷宫坐标
#方便后续递归回溯路径
from collections import deque
dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    inq=set()
    inq.add((x,y))
    pre=[[(-1,-1)]*m for _ in range(n)]
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx==n-1 and ny==m-1:
                    pre[nx][ny]=(x,y)
                    return pre
                if 0<=nx<n and 0<=ny<m and s[nx][ny]==0 and (nx,ny) not in inq:
                    q.append((nx,ny))
                    inq.add((nx,ny))
                    pre[nx][ny]=(x,y)

def printPath(pre,p):
    path=[]
    while p!=(-1,-1):
        path.append(p)
        p=pre[p[0]][p[1]]
    path.reverse()
    for pos in path:
        print(pos[0]+1,pos[1]+1)

n,m=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(n)]
pre=bfs(0,0)
printPath(pre,(n-1,m-1))