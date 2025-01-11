t=int(input())
for _ in range(t):
    move=0
    a,b=map(int,input().split())
    if abs(a-b)>=10:
        move+=abs(a-b)//10
        if abs(a-b)%10!=0:
            move+=1
    elif abs(a-b)<10 and abs(a-b)!=0:
        move+=1
    else:
        move+=0
    print(move)
