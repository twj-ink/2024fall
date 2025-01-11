from heapq import heappop,heappush,heapify
n=int(input())
s=list(map(int,input().split()))
ans=0
heapify(s)
while len(s)>1:
    a=heappop(s)
    b=heappop(s)
    ans+=a+b
    heappush(s,a+b)
print(ans)