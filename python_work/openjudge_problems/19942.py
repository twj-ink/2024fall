m,n,p,q=map(int,input().split())
mn=[list(map(int,input().split())) for _ in range(m)]
pq=[list(map(int,input().split())) for _ in range(p)]
ans=[[0]*(n+1-q) for _ in range(m+1-p)]
for x in range(m+1-p):
    for y in range(n+1-q):
        for i in range(p):
            for j in range(q):
                ans[x][y]+=pq[i][j]*mn[x+i][y+j]
for i in ans:
    print(' '.join(map(str,i)))
