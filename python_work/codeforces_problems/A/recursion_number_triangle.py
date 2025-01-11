'''dfs必须有结束条件
数字三角形 http://cs101.openjudge.cn/practice/02760
目的是找出最大路径和，则递归函数f(i,j)为当前位置向下的所有路径的最大值
而一个位置的最大值由它下面的两条路的值决定，
所以递推式为f(i,j)=max(f(i+1,j),f(i+1,j+1))+tri(i,j)
'''
from functools import lru_cache
@lru_cache(maxsize=None)
def f(i,j):
    if i==n-1:
        return tri[i][j]
    return max(f(i+1,j),f(i+1,j+1))+tri[i][j]

n=int(input())
tri=[[int(i) for i in input().split()] for _ in range(n)]
print(f(0,0))