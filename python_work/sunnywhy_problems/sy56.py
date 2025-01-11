n=int(input())
s=[int(x) for x in input().split()]
if s==sorted(s):
    print('YES')
else:
    print('NO')