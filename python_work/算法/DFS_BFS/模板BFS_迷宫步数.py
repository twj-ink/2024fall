#迷宫1为墙0为地
#不能走出就是-1
#求最小步数，一圈一圈的遍历,算一步，所以在while之后要把q中for循环结束
#因此一旦找到重点就可以退出
from collections import deque

dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    inq=set()
    inq.add((x,y))
    step=0
    while q:
        for _ in range((len(q))):
            x,y=q.popleft()
            if x==n-1 and y==m-1:
                return step
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and s[nx][ny]==0 and (nx,ny) not in inq:
                    q.append((nx,ny))
                    inq.add((nx,ny))
        step+=1
    return -1

n,m=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(n)]
step=bfs(0,0)
print(step)