def around(i,j,s):
    return s[i-1][j-1]+s[i-1][j]+s[i-1][j+1]+s[i][j-1]+s[i][j+1]+s[i+1][j-1]+s[i+1][j]+s[i+1][j+1]

n,m=map(int,input().split())
s=[[0]*(m+2)]+[list(map(int,input().split())) for _ in range(n)]+[[0]*(m+2)]
for i in range(1,n+1):
    s[i].insert(0,0)
    s[i].append(0)
ss=[[0]*m for _ in range(n)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i][j]==1:
            if around(i,j,s)==2 or around(i,j,s)==3:
                ss[i-1][j-1]=1
        else:
            if around(i,j,s)==3:
                ss[i-1][j-1]=1
for i in ss:
    print(*i)

n,m=map(int,input().split())
board=[]
board.append([0]*(m+2))
for _ in range(n):
    board.append([0]+[int(i) for i in input().split()]+[0])
board.append([0]*(m+2))