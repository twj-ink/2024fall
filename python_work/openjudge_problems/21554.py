n=int(input())
t=list(map(int,input().split()))
d=[]
for index,value in enumerate(t):
    d.append([index+1,value])
d.sort(key=lambda x:x[1])
index=[]
ans=0
for i in range(0,n):
    index.append(d[i][0])
    ans+=d[i][1]*(n-i-1)
print(*index)
print(format(ans/n,'.2f'))
