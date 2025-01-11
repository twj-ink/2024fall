# mod=10**9+7
# t,k=map(int,input().split())
# dp=[1]+[0]*(10**5)
# prefix=[0]+[0]*(10**5)
# for i in range(1,10**5+1):
#     if i<k:
#         dp[i]=1
#     else:
#         dp[i]=(dp[i-1]+dp[i-k])
#         dp[i]%=mod
# for i in range(1,10**5+1):
#     prefix[i]=(prefix[i-1]+dp[i])%mod
#
# for _ in range(t):
#     a,b=map(int,input().split())
#     print((prefix[b]-prefix[a-1])%mod)

mod = 10 ** 9 + 7
t, k = map(int, input().split())
prefix = [1] + [0] * (10 ** 5)
for i in range(1, 10 ** 5 + 1):
    if i < k:
        prefix[i] = i + 1
    else:
        last = 1
        curr = last + prefix[i - k]
        prefix[i] = (prefix[i - 1] + curr) % mod
        last = curr % mod

for _ in range(t):
    a, b = map(int, input().split())
    print((prefix[b] - prefix[a - 1]) % mod)

