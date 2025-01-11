n=int(input())
s=list(map(int,input().split()))
ss=[i-520 for i in s]
prefix=0
prefix_map={0:-1}   #值，索引
ans=0

for i in range(n):
    prefix+=ss[i]
    if prefix in prefix_map:
        start=prefix_map[prefix]
        ans=max(ans,520*(i-start))
    else:
        prefix_map[prefix]=i
print(ans)