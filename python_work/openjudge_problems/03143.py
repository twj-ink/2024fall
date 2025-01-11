def is_prime(x):
    if x<=1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

x=int(input())
if x<6 or x%2!=0:
    print('Error!')
else:
    for i in range(2,x//2+1):
        if is_prime(i) and is_prime(x-i):
            print(f'{x}={i}+{x-i}')
