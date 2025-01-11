ans=0
def dfs(n,s,x,y):
    global ans
    if n==1:
        ans=max(ans,s[x][y])
        return
    if n==0:
        return
    curr=0
    d=[(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(4*(n-1)):
        dx,dy=d[(i//(n-1))%4]
        x+=dx;y+=dy
        curr+=s[x][y]
    ans=max(ans,curr)
    dfs(n-2,s,x+1,y+1)

n=int(input())
s=[]
for _ in range(n):
    s.append(list(map(int,input().split())))
dfs(n,s,0,0)
print(ans)
