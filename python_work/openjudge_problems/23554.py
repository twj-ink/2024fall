n=int(input())
s=list(map(int,input().split()))
b=[]
for i in s:
    if i>n:
        b.append(i)
set_n=set(i for i in range(1,n+1))
set_s=set(s)
local=set_n&set_s
missed=set_n-local
a=list(missed)
print(' '.join(map(str,sorted(a))))
print(' '.join(map(str,sorted(b))))
