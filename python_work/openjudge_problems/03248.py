from math import gcd

while True:
    try:
        a,b=map(int,input().split())
        divider=gcd(a,b)
        print(divider)
    except EOFError:
        break
