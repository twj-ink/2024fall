d=int(input())
n=int(input())
point=[];s=[[0]*1025 for _ in range(1025)]
for _ in range(n):
    x,y,z=map(int,input().split())
    point.append((x,y))
    for i in range(max(-x,-d),min(d+1,1024-x+1)):
        for j in range(max(-y,-d),min(d+1,1024-y+1)):
            s[x+i][y+j]+=z
m=0
for i in s:
    m=max(m,max(i))
cnt=0
for i in s:
    cnt+=i.count(m)
print(cnt,m)