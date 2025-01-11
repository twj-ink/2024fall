#递归+记忆+增大递归深度
mod=10**9+7
from functools import lru_cache
import sys
sys.setrecursionlimit(1 << 30)
@lru_cache(maxsize=None)
def f(n):
    if n==1 or n==2:
        return 1
    return f(n-1)%mod+f(n-2)%mod
n=int(input())
print(f(n)%mod)

#dp
mod=10**9+7
def f(n):
    if n==1 or n==2:
        return 1
    dp=[0]*(n+1)
    dp[1]=dp[2]=1
    for i in range(3,n+1):
        dp[i]=dp[i-1]%mod+dp[i-2]%mod
    return dp[n]%mod
n=int(input())
print(f(n)%mod)

#递推
mod=10**9+7
def f(n):
    mod=10**9+7
    a=b=1
    if n==1 or n==2:
        return 1
    for _ in range(n-2):
        a,b=b,(a+b)%mod
    return b
n=int(input())
print(f(n)%mod)

#矩阵快速幂
def matrix_mult(A, B):
    """Multiply two 2x2 matrices."""
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
        ]
    ]

def matrix_pow(mat, p):
    """Raise the matrix to the power p using binary exponentiation."""
    result = [[1, 0], [0, 1]]  # Identity matrix
    while p:
        if p % 2 == 1:
            result = matrix_mult(result, mat)
        mat = matrix_mult(mat, mat)
        p //= 2
    return result

def fibonacci(n):
    """Return the n-th Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        F = [[1, 1], [1, 0]]
        result = matrix_pow(F, n - 1)
        return result[0][0]

# 使用模运算来防止整数溢出
MOD = 10**9+7  # 可以根据需要调整模数

# 输入
n = int(input())
fib_n = fibonacci(n)
print(fib_n)

