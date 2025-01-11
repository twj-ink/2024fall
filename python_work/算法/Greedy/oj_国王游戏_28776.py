n=int(input())
l,_=map(int,input().split())
s=[]
for _ in range(n):
    a,b=map(int,input().split())
    s.append((a*b,a,b))
s.sort(key=lambda x:x[0])
ans=l//s[0][2]
for i in range(1,n):
    l*=s[i-1][1]
    ans=max(ans,l//s[i][2])
print(ans)