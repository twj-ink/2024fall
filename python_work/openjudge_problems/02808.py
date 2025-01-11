m,l=map(int,input().split())
s=set()
for _ in range(l):
    a,b=map(int,input().split())
    c=set(i for i in range(a,b+1))
    s=s|c
print(m-len(s)+1)