n=int(input())
s=[list(map(int,input().split())) for _ in range(n)]
cs=[]
for k in [0,1,2]:
    cnt=0
    for i,value in enumerate(s):
        cnt+=s[i-1][k]
    cs.append(cnt)
print(['YES','NO'][sum(1 for i in cs if i!=0)!=0])

