import math

def euler_sieve(max_num):
    """使用欧拉筛法生成指定范围内的质数集合"""
    is_prime = [True] * (max_num + 1)
    primes = []
    for i in range(2, max_num + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if p * i > max_num:  # 超出范围停止
                break
            is_prime[p * i] = False
            if i % p == 0:  # 确保每个质数只用一次
                break
    return set(primes)

def is_perfect_square(x):
    if x < 0:
        return False
    root = math.isqrt(x)
    return root * root == x, root

n = int(input())
s = list(map(int, input().split()))

# 预先计算所有小于等于 sqrt(最大值) 的质数
max_value = max(s)
max_sqrt = int(math.isqrt(max_value))
prime_set = euler_sieve(max_sqrt)

for i in s:
    perfect_square, root = is_perfect_square(i)
    if perfect_square:
        print('YES' if root in prime_set else 'NO')
    else:
        print('NO')

