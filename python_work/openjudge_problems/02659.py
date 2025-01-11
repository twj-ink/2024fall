a, b, k = map(int, input().split())
cnt = 0
grid = [[0] * b for _ in range(a)]
for _ in range(k):
    r, s, p, t = map(int, input().split())
    p = (p - 1) // 2
    cnt += t
    for i in range(max(1- r, -p), min(1+a-r, p + 1)):
        for j in range(max(1- s, -p), min(1+b-s, p + 1)):
            if t == 1:
                grid[r + i - 1][s + j - 1] += 1
            else:
                grid[r + i - 1][s + j - 1] -= 1
num = 0
for i in grid:
    num += i.count(cnt)
print(num)
