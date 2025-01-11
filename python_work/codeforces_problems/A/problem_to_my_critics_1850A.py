t=int(input())
for _ in range(t):
    n=sorted(list(map(int,input().split())))
    if n[1]+n[2]>=10:
        print('YES')
    else:
        print('NO')
