from heapq import heappop,heappush
from collections import defaultdict
n=int(input())
d1,d2=defaultdict(int),defaultdict(int)
h1,h2=[],[]
for _ in range(n):
    a,l,r=input().split()
    l,r=int(l),int(r)
    if a=='+':
        d1[l]+=1
        d2[r]+=1
        heappush(h1,-l)
        heappush(h2,r)
        if -h1[0]>h2[0]:
            print('YES')
        else:
            print('NO')
    else:
        d1[l]-=1
        d2[r]-=1
        while h1 and not d1[-h1[0]]:
            heappop(h1)
        while h2 and not d2[h2[0]]:
            heappop(h2)
        # print(h1[0],h2[0])
        if h1 and h2 and -h1[0]>h2[0]:
            print('YES')
        else:
            print('NO')