t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    num=0
    for i in [b,c,d]:
        if i > a:
            num+=1
    print(num)
