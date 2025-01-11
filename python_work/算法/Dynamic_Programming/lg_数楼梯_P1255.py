def step(n):
    if n==1 or n==2:
        return n
    a,b=1,2
    for _ in range(n-2):
        a,b=b,a+b
    return b

print(step(int(input())))