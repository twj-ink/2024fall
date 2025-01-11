from collections import deque
import sys
input=sys.stdin.read
dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(s,x,y,i,j,water,m,n):
    q=deque([(x,y,s[x][y])])
    water[x][y]=s[x][y]
    while q:
        x,y,height=q.popleft()
        for _ in range(4):
            nx,ny=x+dx[_],y+dy[_]
            if 0<=nx<m and 0<=ny<n and s[nx][ny]<height and water[nx][ny]<height:
                water[nx][ny]=height
                q.append((nx, ny,height))
def main():
    data=input().split()
    idx = 0
    k = int(data[idx])
    idx += 1
    result = []
    for _ in range(k):
        m, n = map(int, data[idx:idx+2])
        idx += 2
        #矩阵
        s = [list(map(int, data[idx+i*n:idx+(i+1)*n])) for i in range(m)]
        idx += m * n
        #司令部
        i, j = map(int, data[idx:idx+2])
        i-=1;j-=1
        idx += 2
        p = int(data[idx])
        idx += 1
        water=[[0]*n for _ in range(m)]
        #起点
        for _ in range(p):
            x,y=map(int,data[idx:idx+2])
            idx+=2
            x-=1;y-=1
            if s[x][y]<=s[i][j]:
                continue
            bfs(s,x,y,i,j,water,m,n)
        if water[i][j]>0:
            result.append('Yes')
        else:
            result.append('No')
    sys.stdout.write('\n'.join(result) + '\n')
if __name__ == '__main__':
    main()