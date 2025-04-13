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

def chose(n):
    prime=[]
    isprime=[True]*(n+1)
    isprime[0]=isprime[1]=False

    for i in range(2,n+1):
        if isprime[i]:
            prime.append(i)
            for k in range(i**2,n+1,i):
                isprime[k]=False
    return prime

p=chose(10001)
case=0
for _ in range(int(input())):
    case+=1
    s=int(input())
    print(f'Case{case}:')
    ans=[]
    for i in p:
        if i<s and str(i)[-1]=='1':
            ans.append(i)
    if ans: print(*ans)
    else:
        print('NULL')
