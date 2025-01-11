'''dfs
马走日 http://cs101.openjudge.cn/practice/04123
遍历所有点，n*m个，每走一步加1，看看k能不能到n*m
'''
#pylint:skip-file
dx=[-1,1,-2,2,-2,2,-1,1]
dy=[-2,-2,-1,-1,1,1,2,2]
def dfs(x,y,k):
    global num
    if k==total:
        num+=1
        return

    s[x][y]=1
    for _ in range(8):
        nx=x+dx[_]
        ny=y+dy[_]
        if 0<=nx<n and 0<=ny<m:
            if s[nx][ny]==0:
                dfs(nx,ny,k+1)
                s[nx][ny]=0


for _ in range(int(input())):
    num=0
    n,m,x,y=map(int,input().split())
    total=n*m
    s=[[0]*m for _ in range(n)]
    dfs(x,y,1)
    print(num)