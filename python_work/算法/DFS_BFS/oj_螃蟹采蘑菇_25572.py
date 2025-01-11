from collections import deque
dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(x1,y1,type,final):
    if type==1:
        a,b,ddx,ddy=n,n-1,0,1
    else:
        a,b,ddx,ddy=n-1,n,1,0
    q=deque()
    q.append((x1,y1))
    inq=set()
    inq.add((x1,y1))
    while q:
        for _ in range(len(q)):
            x1,y1=q.popleft()
            for i in range(4):
                nx,ny=x1+dx[i],y1+dy[i]
                if 0<=nx<a and 0<=ny<b and (nx,ny) not in inq and \
                        (s[nx][ny],s[nx+ddx][ny+ddy]) in ((0,0),(5,0),(0,5),(0,9),(9,0),(5,9),(9,5)):
                    if (nx,ny)==final or (nx+ddx,ny+ddy)==final:
                        return 'yes'
                    q.append((nx,ny))
                    inq.add((nx,ny))
    return 'no'

n=int(input())
s=[];x1=-1
for i in range(n):
    l=list(map(int,input().split()))
    if 9 in l:
        ey=l.index(9)
        final=(i,ey)
    if 5 in l and x1==-1:
        y1=l.index(5)
        x1=i
        type=1 if y1+1<n and l[y1+1]==5 else 2
    s.append(l)
if n==1 or n==0:
    print('no')
else:
    print(bfs(x1,y1,type,final))
