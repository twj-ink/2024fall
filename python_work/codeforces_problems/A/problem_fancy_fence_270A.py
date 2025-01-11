n=int(input())
for _ in range(n):
    s=int(input())
    if 360%(180-s)==0:
        print('YES')
    else:
        print('NO')