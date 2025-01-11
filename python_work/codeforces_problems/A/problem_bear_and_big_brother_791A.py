a,b=map(int,input().split())
turn=0
while a<=b:
    a=a*3
    b=b*2
    turn+=1
print(turn)

#while循环的使用：不断操作直到满足条件