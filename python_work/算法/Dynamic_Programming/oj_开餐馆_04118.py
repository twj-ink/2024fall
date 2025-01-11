from bisect import bisect_right

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    # dp=list(map(int, input().split()))
    # for i in range(1,n):
    #     if (index:=bisect_right(m,m[i]-k-1))!=0:
    #         curr=dp[i]
    #         for j in range(index):
    #             curr=max(dp[i]+dp[j],curr)
    #         dp[i]=curr
    # print(max(dp))
    p=list(map(int,input().split()))
    dp_max_so_far=[0]*n
    dp_max_so_far[0]=p[0]
    for i in range(1,n):
        if (index:=bisect_right(m,m[i]-k-1))>0:
            p[i]+=dp_max_so_far[index-1]
        dp_max_so_far[i]=max(dp_max_so_far[i-1],p[i])
    print(dp_max_so_far[-1])