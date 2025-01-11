n=int(input())
num=0
for _ in range(n):
    a,b=map(int,input().split())
    rest=b-a
    if rest>=2:
        num+=1
print(num)
