n=int(input())
count=0
for _ in range(n):
    a,b=map(int,input().split())
    if a>b:
        count+=1
    elif a<b:
        count-=1
if count==0:
    print("Friendship is magic!^^")
elif count>0:
    print("Mishka")
else:
    print('Chris')