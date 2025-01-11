t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ab=[]
    for i in range(n):
        ab.append((a[i],b[i]))
    ab.sort(key=lambda x:x[0])
    ans=[]
    m=sum(ab[j][1] for j in range(0,n))
    ans.append(m)
    for i in range(n-1):
        m-=ab[i][1]
        ans.append(max(ab[i][0],m))
    ans.append(sum(ab[i][1] for i in range(0,n)))
    ans.append(ab[-1][0])
    print(min(ans))