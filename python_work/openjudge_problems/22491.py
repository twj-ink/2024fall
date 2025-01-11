h=int(input())
m=int(input())
h=2*h-(0.5*m)
sc=[]
ans,i=0,0
for _ in range(m):
    s,c=map(float,input().split())
    sc.append((s*c,s,c))
sc.sort(reverse=True)
while h>=0 and i<m:
    if h>=5/sc[i][1]:
        ans+=5*sc[i][2]
        h-=5/sc[i][1]
        i+=1
    else:
        ans+=h*sc[i][0]
        break
print(format(ans,'.1f'))
