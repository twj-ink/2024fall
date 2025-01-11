n,m=map(int,input().split())
day=0
while n>0:
    day+=1
    n-=1
    if day%m==0:
        n+=1
print(day)

