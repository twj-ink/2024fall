def getMaxBenefit(cut,v):
    c=0
    for i in range(len(cut)):
        if cut[i][0]>v:
            break
        c=max(c,cut[i][1])
    return c

ans=[]
def dfs(k,shop,curr1,curr2):
    global ans
    if k==n:
        for i in range(m):
            v=shop[i]
            curr2+=v
            real_v=v-getMaxBenefit(cut[i],v)
            curr1+=real_v
        curr1-=50*(curr2//300)
        ans.append(curr1)
        curr1=curr2=0
        return

    for i in range(len(goods[k])):
        shop[goods[k][i][0]-1]=shop[goods[k][i][0]-1]+goods[k][i][1]
        dfs(k+1,shop,curr1,curr2)
        shop[goods[k][i][0]-1]=shop[goods[k][i][0]-1]-goods[k][i][1]

n,m=map(int,input().split())
goods=[[] for _ in range(n)]
shop=[0]*m
cut=[[] for _ in range(m)]
for i in range(n):
    s=list(input().split())
    for j in s:
        a,b=map(int,j.split(':'))
        goods[i].append((a,b))
for i in range(m):
    s=list(input().split())
    for j in s:
        a,b=map(int,j.split('-'))
        cut[i].append((a,b))
    cut[i].sort(key=lambda x:x[0])
dfs(0,shop,0,0)
print(min(ans))
