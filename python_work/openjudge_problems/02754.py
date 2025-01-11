chosen=[False]*9
ans=[0]*9
result=[]
def dfs(k):
    global result
    if k>8:
        result.append(ans[1:])
    for i in range(1,9):
        if chosen[i]:
            continue
        f=False
        for j in range(1,k):
            if abs(ans[j]-i)==abs(j-k):
                f=True
                break
        if f:
            continue
        chosen[i]=True
        ans[k]=i
        dfs(k+1)
        chosen[i]=False
dfs(1)
#print(result)
n=int(input())
for _ in range(n):
    t=int(input())
    print(''.join(map(str,result[t-1])))