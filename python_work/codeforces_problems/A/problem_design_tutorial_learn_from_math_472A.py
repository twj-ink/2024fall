def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input())
half_n=int(n/2)
for i in range(4,half_n+1):
    if is_prime(i) or is_prime(n-i):
        continue
    else:
        print(str(i)+' '+str(n-i))
        break
