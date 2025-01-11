t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(0,n):
        if n>=2**i and n<2**(i+1):
            answer=(n*(n+1))//2+2-2**(i+2)
            print(answer)
            break