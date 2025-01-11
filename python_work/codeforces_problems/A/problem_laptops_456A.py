n=int(input())
ab=[]
for _ in range(n):
    a,b=map(int,input().split())
    ab.append((a,b))
ab.sort()
flag=False
i=j=0
while i<n-1:
    if ab[i+1][1]<ab[j][1]:
        flag=True
        break
    else:
        j=i+1
        i+=1
if flag==True:
    print('Happy Alex')
else:
    print('Poor Alex')