i=1
while True:
    a,b,c,d=map(int,input().split())
    if {a,b,c,d}=={-1}:
        break
    flag=True
    while flag:
        a+=23
        if (a-b)%28==0 and (a-c)%33==0:
            flag=False
    print(f'Case {i}: the next triple peak occurs in {a-d} days.')
    i+=1