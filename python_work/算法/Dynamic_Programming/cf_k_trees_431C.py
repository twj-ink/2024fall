#把n用不大于k的数字划分的个数 - 把n用小于d的数字划分的个数
#划分要考虑话分数的顺序
mod=10**9+7
n,k,d=map(int,input().split())
dp_k=[1]+[0]*n
dp_d=[1]+[0]*n
for i in range(1,n+1):
    for j in range(1,min(i+1,k+1)):
        dp_k[i]=(dp_k[i]+dp_k[i-j])%mod
    for j in range(1,min(i+1,d)):
        dp_d[i]=(dp_d[i]+dp_d[i-j])%mod
print((dp_k[-1]-dp_d[-1])%mod)

# n,k,d=map(int,input().split())
# mod = 10**9 + 7
# # A[i]：总权重为i的路径数 ； B[i]：总权重为i且所有边权重小于d的路径数
# A = [1] + [0] * n
# B = [1] + [0] * n
# # 路径数本质上就是整数划分问题
# # 本题即求用不大于k的正整数划分i，用小于d的正整数划分i的方法数之差
# for i in range(1, n + 1):
#     for j in range(1, min(i,k)+1):
#         A[i] = (A[i] + A[i - j]) % mod
#     for j in range(1, min(d, i + 1)):
#         B[i] = (B[i] + B[i - j]) % mod
# print((A[n] - B[n]) % mod)
# print(A,B)