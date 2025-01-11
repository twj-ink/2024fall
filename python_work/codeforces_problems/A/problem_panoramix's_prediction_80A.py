def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n,m=map(int,input().split())
if not is_prime(m):
    print('NO')
else:
    found_prime_between=False
    for i in range(n+1,m):
        if is_prime(i):
            found_prime_between=True
            break
    if found_prime_between:
        print('NO')
    else:
        print('YES')