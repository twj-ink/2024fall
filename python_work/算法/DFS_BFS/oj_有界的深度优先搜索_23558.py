def dfs(n,m,l,s,ans,k):
    if k==l+1 or s not in d:
        return
    for i in d[s]:
        if not visited[i] and i not in ans:
            visited[i]=1
            ans.append(i)
            dfs(n,m,l,i,ans,k+1)
            visited[i]=0


n,m,l=map(int,input().split())
d={};dd={}
for _ in range(m):
    a,b=map(int,input().split())
    if a>b: a,b=b,a
    if a not in d:
        d[a]=[]
    d[a].append(b)
    if b not in d:
        d[b]=[]
    d[b].append(a)
    # if b not in dd:
    #     dd[b]=[]
    # dd[b].append(a)
for v in d.values():
    v.sort()
# for v in dd.values():
#     v.sort()
s=int(input())
visited=[0]*n
ans=[s]
visited[s]=1
# print(d)
dfs(n,m,l,s,ans,1)
print(*ans)