n,m=map(int,input().split())
s=sorted(list(map(int,input().split())))
total=s[-1]-s[0]
delta=[]
for i in range(n-1):
    delta.append(s[i+1]-s[i])
delta.sort(reverse=True)
print(total-sum(delta[:m-1]))
#用总间隔减去最大的几个间隔