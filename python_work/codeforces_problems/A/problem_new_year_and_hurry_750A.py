n,k=map(int,input().split())
rest=240-k
maximum=0
for i in range(1,n+1):
    if ((i+1)*i/2)*5<=rest:
        maximum+=1
print(maximum)