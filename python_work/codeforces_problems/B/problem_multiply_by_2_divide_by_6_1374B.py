t=int(input())
for _ in range(t):
    b=c=0
    n=m=int(input())
    while m%3==0:
        m//=3
        b+=1
    while m%2==0:
        m//=2
        c+=1
    if m!=1:
        print('-1')
    else:
        if c>b:
            print('-1')
        else:
            print(2*b-c)

