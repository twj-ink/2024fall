t=int(input())
for _ in range(t):
    n=int(input())
    if n%2!=0:
        print('YES')
    else:
        while n%2==0:
            n/=2
        if n==1:
            print('NO')
        else:
            print('YES')