'''bfs
数字操作 https://sunnywhy.com/sfbj/8/2/318
'''
from collections import deque
def bfs(n):
    inq=set()
    inq.add(1)
    q=deque()
    q.append((0,1)) #(step,front)
    while q:
        step,front=q.popleft()
        if front==n:
            return step
        if front*2<=n and front*2 not in inq:
            inq.add(front*2)
            q.append((step+1,front*2))
        if front+1<=n and front+1 not in inq:
            inq.add(front+1)
            q.append((step+1,front+1))
n=int(input())
print(bfs(n))
