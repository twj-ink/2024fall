import heapq
dx,dy=[0,-1,1,0],[-1,0,0,1]
def dijkstra(sx,sy,ex,ey):
    if s[sx][sy]=='#' or s[ex][ey]=='#':
        return 'NO'
    q=[]
    dist=[[float('inf')]*m for _ in range(n)]
    heapq.heappush(q,(0,sx,sy)) #(distance,x,y)
    dist[sx][sy]=0
    while q:
        curr,x,y=heapq.heappop(q)
        if (x,y)==(ex,ey):
                return curr

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and s[nx][ny]!='#':
                new=curr+abs(s[x][y]-s[nx][ny])
                if new<dist[nx][ny]:
                    heapq.heappush(q,(new,nx,ny))
                    dist[nx][ny]=new
    return 'NO'

n,m,p=map(int,input().split())
s=[]
for i in range(n):
    line=input().split()
    for j in range(m):
        if line[j]!='#':
            line[j]=int(line[j])
    s.append(line)
for _ in range(p):
    sx,sy,ex,ey=map(int,input().split())
    print(dijkstra(sx,sy,ex,ey))