from collections import deque
dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(s,x,y,step):
    q=deque()
    q.append((x,y,step))
    inq=set()
    inq.add((x,y,step))
    while q:
        for _ in range(len(q)):
            x,y,step=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and (nx,ny,(step+1)%k) not in inq:
                    if s[nx][ny]=='E':
                        return step+1
                    if ((step+1)%k!=0 and s[nx][ny]!='#') or ((step+1)%k==0):
                        q.append((nx,ny,step+1))
                        inq.add((nx,ny,(step+1)%k))

    return "Oop!"

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    s=[input() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if s[i][j]=='S':
                print(bfs(s,i,j,0))
