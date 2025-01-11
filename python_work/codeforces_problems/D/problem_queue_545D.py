n=int(input())
t=sorted(list(map(int,input().split())))
if n==1:
    print(1)
elif n==2:
    if t[0]<=t[1]:
        print(2)
    else:
        print(0)
else:
    dp=[0]*n
    dp[1]=t[0]
    i=2;j=0;cur_j=0
    while i<n:
        if dp[i-1-cur_j]+t[i-1-cur_j]<=t[i]:
            dp[i]=dp[i-1-cur_j]+t[i-1-cur_j]
            cur_j=0
        else:
            cur_j+=1
            j+=1
        i+=1
    print(n-j)
