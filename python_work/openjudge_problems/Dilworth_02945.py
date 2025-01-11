'''
导弹拦截
https://www.luogu.com.cn/problem/P1020
'''
#第一问 最长不升子序列 reverse right
#第二问 最少不升子列数=最长不降子列长 无需相同 left

from bisect import bisect_left, bisect_right

def doit():
    s=list(map(int,input().split()))
    s.reverse()
    lnis=[]
    for i in s:
        pos=bisect_right(lnis,i)
        if pos<len(lnis):
            lnis[pos]=i
        else:
            lnis.append(i)
    print(len(lnis))

    l2=[]
    s.reverse()
    for i in s:
        p=bisect_left(l2,i)
        if p<len(l2):
            l2[p]=i
        else:
            l2.append(i)
    print(len(l2))

doit()

