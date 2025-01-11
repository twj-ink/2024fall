n,k=map(int,input().split())
s=sorted(list(map(int,input().split())),reverse=True)
total=sum(s)
for i in range(n):
    if s[i]<=total/k:
        break
    else:
        total-=s[i]
        k-=1
print(format(eval('total/k'),'.3f'))