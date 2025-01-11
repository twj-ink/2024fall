n=int(input())
a=sorted(list(map(int,input().split())))
m=int(input())
b=sorted(list(map(int,input().split())))
cnt=i=j=0
curj=[]
while i<n:
    while j<m and i<n:
        if abs(a[i]-b[j])<=1:
            cnt+=1;i+=1;j+=1
            curj.append(j)
        else:
            j+=1
    i+=1
    if curj:
        j=curj[-1]
    else:
        j=0
print(cnt)
