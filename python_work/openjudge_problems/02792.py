n=int(input())
for _ in range(n):
    cnt=0
    s=int(input())
    a=int(input())
    numa=list(map(int,input().split()))
    b=int(input())
    numb=sorted(list(map(int,input().split())))
    for i in numa:
        flag=False
        left,right=0,len(numb)-1
        while left <= right:
            mid=(left+right)//2
            if numb[mid]+i<s:
                left=mid+1
            elif numb[mid]+i>s:
                right=mid
            else:
                flag=True
                break
        if flag:
            cnt+=numb.count(numb[mid])
    print(cnt)
''''''
from bisect import bisect_left, bisect_right

n = int(input())
for _ in range(n):
    cnt = 0
    s = int(input())
    a = int(input())
    numa = list(map(int, input().split()))
    b = int(input())
    numb = sorted(list(map(int, input().split())))

    for i in numa:
        # 寻找 numb 中所有和 i 的和为 s 的元素范围
        target = s - i
        left = bisect_left(numb, target)
        right = bisect_right(numb, target)

        # 区间内的所有元素都符合条件
        cnt += (right - left)

    print(cnt)
''''''
from collections import Counter

n = int(input())
for _ in range(n):
    cnt = 0
    s = int(input())
    a = int(input())
    numa = list(map(int, input().split()))
    b = int(input())
    numb = list(map(int, input().split()))

    # 使用 Counter 统计 numb 中每个数的出现频次
    counter_b = Counter(numb)

    # 对于 num_a 中的每个数 i，查找 s - i 是否存在于 numb 中
    for i in numa:
        cnt += counter_b[s - i]

    print(cnt)