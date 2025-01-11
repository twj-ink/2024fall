n,h=map(int,input().split())
heights=list(map(int,input().split()))
width=0
for i in heights:
    if i <= h:
        width+=1
    else:
        width+=2
print(width)