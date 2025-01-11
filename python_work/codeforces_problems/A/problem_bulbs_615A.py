n,m=map(int,input().split())
check=[]
for _ in range(n):
    s=list(map(int,input().split()))
    check.extend(s[1:])
if len(set(check))==m:
    print('YES')
else:
    print('NO')