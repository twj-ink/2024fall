t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    min_a=min(a)*n+sum(b)
    min_b=min(b)*n+sum(a)
    if min_a>=min_b:
        print(min_b)
    else:
        print(min_a)
