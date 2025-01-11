n,k=map(int,input().split())
for _ in range(k):
    if str(n)[-1]=='0':
        n=int(str(n)[:-1])
    else:
#        n=str(n)[:-1]+str(int(str(n)[-1])-1)
        n=n-1
print(int(n))

n,k=map(int,input().split())
for _ in range(k):
    if n%10==0:
        n//=10
    else:
        n-=1
print(n)
