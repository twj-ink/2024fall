'''
螺旋矩阵 http://cs101.openjudge.cn/practice/18106
'''
n=int(input())
protect=[[1000]*(n+2)]
mx=protect+[[1000]+[0]*n+[1000] for _ in range(n)]+protect

direction=[[0,1],[1,0],[0,-1],[-1,0]]

x,y,k=1,1,0
dx,dy=direction[0]

for j in range(1,n**2+1):
    mx[x][y]=j
    if mx[x+dx][y+dy]:
        k+=1
        dx,dy=direction[k%4]
    x+=dx
    y+=dy
for i in range(1,n+1):
    print(' '.join(map(str,mx[i][1:-1])))