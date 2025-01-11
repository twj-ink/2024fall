'''bfs
寻宝 http://cs101.openjudge.cn/practice/19930
'''
from collections import deque
dx,dy=[0,-1,1,0],[-1,0,0,1]

def bfs(x,y):
    inq=set()
    inq.add((x,y))
    q=deque()
    q.append((0,x,y))
    if maze[x][y]==1:
        return 0
    while q:
        front=q.popleft()
        for i in range(4):
            nx=front[1]+dx[i]
            ny=front[2]+dy[i]
            if maze[nx][ny]==0 and (nx,ny) not in inq:
                inq.add((nx,ny))
                q.append((front[0]+1,nx,ny))
            if maze[nx][ny]==1 and (nx,ny) not in inq:
                return front[0]+1
    return 'NO'

n,m=map(int,input().split())
maze=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for _ in range(n)]+[[-1]*(m+2)]
result=bfs(1,1)
print(result)