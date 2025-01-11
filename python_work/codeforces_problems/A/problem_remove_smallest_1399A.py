def is_dis1(s, x):
    return s[x + 1] - s[x] <= 1

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if all(is_dis1(s, i) for i in range(0, n - 1)):
        print('YES')
    else:
        print('NO')

def is_dis1(s,x):
    return s[x+1]-s[x]<=1
def is_solve(s):
    return all(is_dis1(s,x) for x in range(len(s-1)))

t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    if is_solve(s):
        print('YES')
    else:
        print('NO')
