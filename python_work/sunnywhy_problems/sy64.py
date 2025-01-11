n=int(input())
s=list(map(int,input().split()))
k=int(input())
cnt=0
for i in s:
    for j in s:
        if i!=j and i+j==k:
            cnt+=1
print(cnt//2)