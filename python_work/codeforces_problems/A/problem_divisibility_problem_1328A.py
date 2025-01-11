##超时
#t=int(input())
#for _ in range(t):
#    move=0
#    a,b=map(int,input().split())
#    while a%b != 0:
#        a+=1
#        move+=1
#    print(move)

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a%b==0:
        print(0)
    else:
        print(b-a%b)