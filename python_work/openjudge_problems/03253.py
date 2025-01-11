while True:
    n,p,m=map(int,input().split())
    if {n,p,m}=={0}:
        break
    s=list(range(1,n+1))
    ans,i=[],0
    for _ in range(p-1):
        s.append(s.pop(0))
    while s:
        i+=1
        curr=s.pop(0)
        if i==m:
            ans.append(curr)
            i=0
        else:
            s.append(curr)
    print(','.join(map(str,ans)))