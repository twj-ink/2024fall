from collections import defaultdict
mp=defaultdict(int)
n,q=map(int,input().split())
for _ in range(q):
    xy=tuple(sorted(map(int,input().split())))
    mp[xy]+=1
if all(v<=1 for v in mp.values()):
    print('No')
else:
    print('Yes')

