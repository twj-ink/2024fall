 #模板：最长上升子列 left
#该题：最少不降子列数==最长不升子列长 reverse(上升) right
##由于刚开始还不是有序数列，先对l排序，得到的w的数列就是有序的数列
##然后对w找到最长不升子序列
###但是这里相同元素无需重复考虑，所以使用left
from bisect import bisect_left,bisect_right

def doit():
    n=int(input())
    data=list(map(int,input().split()))
    sticks=[(data[i],data[i+1]) for i in range(0,2*n,2)]
    sticks.sort()

    w=[sticks[i][1] for i in range(n)]
    w.reverse()
    lnis=[]

    for i in w:
        pos=bisect_left(lnis,i)
        if pos<len(lnis):
            lnis[pos]=i
        else:
            lnis.append(i)
    print(len(lnis))

t=int(input())
for _ in range(t):
    doit()