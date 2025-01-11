abc=list(map(int,input().split()))
abc.sort()
s=abc[3]
a=s-abc[0]
b=s-abc[1]
c=s-abc[2]
print(a,b,c)