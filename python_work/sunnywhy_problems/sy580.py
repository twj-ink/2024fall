n,m=map(int,input().split())
nm=[list(map(int,input().split())) for _ in range(n)]
ans=[]
for i in range(n):
    for j in range(m):
        ans.append(nm[i][j]* \
                   int(str(nm[0][j])+str(nm[i][m-1])+ \
                       str(nm[n-1][j])+str(nm[i][0])))
print(max(ans))