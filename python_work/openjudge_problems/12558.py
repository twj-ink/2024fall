import sys
sys.setrecursionlimit(30000)

def f(i,j,a,b):
    s[i][j]=2
    minus_cnt,land_cnt=0,0
    dx=[0,-1,1,0]
    dy=[-1,0,0,1]
    for d in range(4):
        x=i+dx[d]
        y=j+dy[d]
        if 0<=x<=n-1 and 0<=y<=m-1:
            #额外查看四周有没有重叠边，记录下来
            if s[x][y]==1 or s[x][y]==2:
                minus_cnt+=1
            if s[x][y]==1:
                f(x,y,a,b)
                land_cnt+=1

    a.append(minus_cnt)
    b.append(land_cnt)

n,m=map(int,input().split())
s=[[int(i) for i in input().split()] for _ in range(n)]
a,b,result=[],[],0
for i in range(n):
    for j in range(m):
        if s[i][j]==1:
            f(i,j,a,b)
            #如果没有陆地就保持初始值0，否则加初始的1个
            if b:
                b.append(1)
            result+=4*sum(b)-sum(a)
            a,b=[],[]
print(result)