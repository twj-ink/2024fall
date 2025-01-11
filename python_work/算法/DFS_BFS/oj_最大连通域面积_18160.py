'''dfs
最大连通域面积 http://cs101.openjudge.cn/practice/18160
函数的作用是每找到一个点就把一片修改，同时计数
返回值是一片的个数
要二重循环
'''
#pylint:skip-file
def dfs(i,j):
    global cnt
    s[i][j]='.'
    cnt+=1
    dx=[-1,0,1,-1,1,-1,0,1]
    dy=[-1,-1,-1,0,0,1,1,1]
    for _ in range(8):
        x=i+dx[_]
        y=j+dy[_]
        if 0<=x<=n-1 and 0<=y<=m-1:
            if s[x][y]=='W':
                dfs(x,y)
    return cnt


for _ in range(int(input())):
    n,m=map(int,input().split())
    a=0
    s=[[i for i in input()] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if s[i][j]=='W':
                cnt=0
                ans=dfs(i,j)
                a=max(ans,a)

    print(a)
