'''
跳高 http://cs101.openjudge.cn/2024fallroutine/28389/
Dilworth 定理:
 Dilworth 定理表明，任何一个有限偏序集的最长反链(即最长下降子序列)的长度，
等于将该偏序集划分为尽量少的链(即上升子序列)的最小数量。
因此，计算序列的最长下降子序列长度，即可得出最少需要多少台测试仪。
即：求最少的上升子序列的个数=最长的下降子序列的长度
'''
##最少单调链个数===最长反单调链长度
#模板：找最长上升子序列，用left
#这道题是：找最长下降子序列，先reverse，再用left
#如果是不降，用right
#如果是不升，先reverse，再用right
###看题目要求的最终结果是否需要相同元素的考虑，需要考虑用left
###不需要用right

from bisect import bisect_left

def min_needed(scores):
    scores.reverse()
    lis=[]
    for score in scores:
        pos=bisect_left(lis,score)
        if pos<len(lis):
            lis[pos]=score
        else:
            lis.append(score)
    return len(lis)
n=int(input())
scores=list(map(int,input().split()))
result=min_needed(scores)
print(result)

5
1 7 3 5 2

3
(752)