check=[2**i for i in range(0,12)]

q=int(input())
for _ in range(q):
    n=int(input())
    s=list(map(int,input().split()))
    a=[]
    for i in check:
        a.append(s.count(i))
    if a[-1]:
        print('yes')
    else:
        for i in range(0,11):
            a[i+1]+=a[i]//2
        if a[-1]:
            print('yes')
        else:
            print('NO')