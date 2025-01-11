def step(n):
    if n==1 or n==2:
        return n
    dp=[1,2]+[0]*(n-2)
    for i in range(2,n):
        dp[i]=1+sum(dp[j] for j in range(i))
    return dp[-1]

print(step(int(input())))