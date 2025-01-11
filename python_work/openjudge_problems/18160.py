def matrix(n,result,k,start):
    if n==1 or (n%2==1 and k+1==n):
        result[n//2][n//2]=n**2
        return result
    if n==2 or (n%2==0 and k+2==n):
        center=n//2
        d=[(-1,-1,3),(-1,0,2),(0,-1,0),(0,0,1)]
        for x,y,c in d:
            result[center+x][center+y]=n**2-c
        return result

    for i in range(k-1,n-k):
        result[k-1][i]=start+i-(k-2 if k>2 else 0)

    for j in range(k-1,n-k):
        result[j][n-k]=result[k-1][n-k-1]+j-(k-2)

    for i in range(k-1,n-k):
        result[n-k][n-i-1]=result[n-k-1][n-k]+i-(k-2)

    for j in range(k-1,n-k):
        result[n-j-1][k-1]=result[n-k][k]+j-(k-2)

    start=result[k][k-1]
    k+=1
    matrix(n,result,k,start)
    return result

n=int(input())
result=[[0]*n for _ in range(n)]
k,start=1,1
ans=matrix(n,result,k,start)
for i in ans:
    print(*i)

'''
螺旋矩阵 http://cs101.openjudge.cn/practice/18106
设置方向向量
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