m=int(input())
for _ in range(m):
    a,b,c,d=map(int,input().split())
    found=False
    for i in [a,-a]:
        for j in [b,-b]:
            for k in [c,-c]:
                for l in [d,-d]:
                    if i+j+k+l==24:
                        print('YES')
                        found=True
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    if not found:
        print('NO')

from itertools import permutations as p
m=int(input())
for _ in range(m):
    a,b,c,d=map(int,input().split())
    s=[p([a,b,c,d],4)]
    for i in s:
        res1 = i[0] + i[1] + i[2] - i[3]
        res2 = i[0] + i[1] - i[2] - i[3]
        res3 = i[0] - i[1] - i[2] - i[3]
        res4 = i[0] + i[1] + i[2] + i[3]
        if res4 == 24 or res1 == 24 or res2 == 24 or res3 == 24:
            print('YES')
            break
    else:
        print('NO')