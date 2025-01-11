import timeit

# 定义代码块
code_to_test = """
def euler_sieve(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是质数

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)  # i 是质数
        for prime in primes:
            if i * prime > n:
                break
            is_prime[i * prime] = False
            # 如果 prime 是 i 的最小质因数，停止继续筛选
            if i % prime == 0:
                break
    
    return primes
euler_sieve(100)
"""

# 使用 timeit 测量代码的运行时间，默认运行 1,000,000 次
execution_time = timeit.timeit(code_to_test, number=1000)

# 输出运行时间
print(f"运行时间: {execution_time} 秒")