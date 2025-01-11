turn=1
n=int(input())
cards=list(map(int,input().split()))
sere=[]
dima=[]
while len(cards) != 0:
    m=max(cards[0],cards[-1])
    cards.remove(m)
    if turn%2 != 0:
        sere.append(m)
    else:
        dima.append(m)
    turn+=1
sum1=sum(sere)
sum2=sum(dima)
print(str(sum1)+' '+str(sum2))
