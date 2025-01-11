'''dfs必须有退出条件
Lake Counting http://cs101.openjudge.cn/practice/02386
但是没有回溯，只有向前递
'''
import sys
sys.setrecursionlimit(20000)
def f(i,j):
    m[i][j]='.'
    dx=[-1,0,1,-1,1,-1,0,1]
    dy=[-1,-1,-1,0,0,1,1,1]
    for k in range(8):
        x=i+dx[k]
        y=j+dy[k]
        if 0<=x<=n-1 and 0<=y<=s-1:
            if m[x][y]=='W':
                f(x,y)

n,s=map(int,input().split())
m=[[i for i in input()] for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(s):
        if m[i][j]=='W':
            f(i,j)
            cnt+=1
print(cnt)