n=int(input())
a=list(map(int,input().split()))
b=[];count=1
for i in range(0,n-1):
    if a[i+1]>=a[i]:
        count+=1
    else:
        b.append(count)
        count=1
b.append(count)
print(max(b))