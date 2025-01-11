'''dfs必须有退出条件
晶矿的个数 http://cs101.openjudge.cn/practice/05585
但是没有回溯，只有向前递
'''
def f(i,j,mine):
    m[i][j]='#'
    dx=[0,-1,1,0]
    dy=[-1,0,0,1]
    for k in range(4):
        x=i+dx[k]
        y=j+dy[k]
        if 0<=x<=n-1 and 0<=y<=n-1:
            if m[x][y]==mine:
                f(x,y,mine)

for _ in range(int(input())):
    n=int(input())
    m=[[i for i in input()] for _ in range(n)]
    cntr,cntb=0,0
    for i in range(n):
        for j in range(n):
            if m[i][j]=='r':
                f(i,j,'r')
                cntr+=1
            if m[i][j]=='b':
                f(i,j,'b')
                cntb+=1
    print(cntr,cntb)

