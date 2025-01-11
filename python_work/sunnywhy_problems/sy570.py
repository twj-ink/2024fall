n,q=map(int,input().split())
grid=[[0]*(n+2) for _ in range(n+2)]
flag=False
for _ in range(q):
    x,y=map(int,input().split())
    grid[x][y]=1
    for i in range(n+2):
        if grid[y][i]==grid[i][x]==1:
            flag=True
if flag:
    print('Yes')
else:
    print('No')