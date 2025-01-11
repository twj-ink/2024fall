n=int(input())
for _ in range(n):
    x=int(input())
    if x<=2:
        print(0)
    else:
        if x%2==0:
            print(int(x/2-1))
        else:
            print(int(x//2))