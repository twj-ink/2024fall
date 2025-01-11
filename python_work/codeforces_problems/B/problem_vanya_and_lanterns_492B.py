n,l=map(int,input().split())
a=sorted(list(map(int,input().split())))
a.insert(0,0)
a.append(l)
m1=a[1]-a[0]
m2=a[-1]-a[-2]
m=max(m1,m2)
for i in range(2,n+1):
    m=max(m,max(m1,(a[i]-a[i-1])/2))
print(m)