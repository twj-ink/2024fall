from functools import lru_cache

@lru_cache
def path_sum(i,j,n):
    if i==n-1:
        return a[i][j]
    return a[i][j]+max(path_sum(i+1,j,n),path_sum(i+1,j+1,n))
t=int(input())
a=[[int(_) for _ in input().split()] for _ in range(t)]
print(path_sum(0,0,t))