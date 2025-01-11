n=int(input())
money=list(map(int,input().split()))
if len(money)==1:
    print('0')
else:
    m=max(money)
    need=[]
    for i in money:
        need.append(m-i)
    total=sum(need)
    print(total)

