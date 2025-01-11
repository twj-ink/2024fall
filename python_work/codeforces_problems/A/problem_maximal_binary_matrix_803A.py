n,k=map(int,input().split())
if k>n*n:
    print(-1)
else:
    s=[[0]*n for _ in range(n)]
    for i in range(0,n):
        if k==0:
            break
        for j in range(0,n):
            if k==0:
                break
            if s[i][j]==1:
                continue
            if i==j and k>=1:
                s[i][j]=1
                k-=1
            else:
                if k>=2:
                    s[i][j]=s[j][i]=1
                    k-=2

    for i in s:
        print(*i)
