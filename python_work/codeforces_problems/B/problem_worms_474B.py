n=int(input())
piles=list(map(int,input().split()))
m=int(input())
queries=list(map(int,input().split()))
#for i in j:
#    count=1
#    k=0
#    while i>nums[k]:
#        count+=1
#        i-=nums[k]
#        k+=1
#    print(count)
prefix_sums = [0] * n
prefix_sums[0] = piles[0]
for i in range(1, n):
    prefix_sums[i] = prefix_sums[i - 1] + piles[i]

# 对每个查询进行处理
for q in queries:
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if prefix_sums[mid] < q:
            left = mid + 1
        else:
            right = mid
    # 输出1-based索引
    print(left + 1)