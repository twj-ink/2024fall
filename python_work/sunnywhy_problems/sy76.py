n,k=map(int,input().split())
stack=[]
ans=''
l='0123456789ABCDEF'
while n!=0:
    stack.append(n%k)
    n//=k
while stack:
    ans+=l[stack.pop()]
print(ans)