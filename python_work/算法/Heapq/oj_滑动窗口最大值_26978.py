import heapq
# from collections import deque
n,k=map(int,input().split())
s=list(map(int,input().split()))
heap,ans=[],[]
for i in range(n):
    heapq.heappush(heap,(-s[i],i))
    while heap[0][1]<=i-k:
        heapq.heappop(heap)
    if i>=k-1:
        ans.append(-heap[0][0])
print(*ans)