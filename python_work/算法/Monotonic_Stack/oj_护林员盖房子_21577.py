def house(mat,n,m):
    prefix=[[0]*(m+2) for _ in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            prefix[i][j]=0 if mat[i-1][j-1]==1 else prefix[i-1][j]+1

    ans=0
    for i in range(1,n+1):
        ans_=0
        stack=[0]
        for j in range(1,m+2):
            while stack and prefix[i][j]<prefix[i][stack[-1]]:
                curr_h=prefix[i][stack.pop()]
                curr_w=j-stack[-1]-1
                ans_=max(ans_,curr_h*curr_w)
            stack.append(j)
        ans=max(ans,ans_)
    return ans
n,m=map(int,input().split())
mat=[[int(i) for i in input().split()] for _ in range(n)]
print(house(mat,n,m))