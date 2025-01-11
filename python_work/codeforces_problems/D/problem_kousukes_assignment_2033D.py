import sys
input=lambda: sys.stdin.readline()

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = 0
    prefixed = {0}
    cnt = 0
    for i in a:
        prefix += i
        if prefix not in prefixed:
            prefixed.add(prefix)
        else:
            cnt += 1
            prefix = 0
            prefixed={0}
    print(cnt)