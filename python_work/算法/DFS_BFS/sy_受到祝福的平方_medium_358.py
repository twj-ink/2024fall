'''dfs
受到祝福的平方 中等 https://sunnywhy.com/sfbj/8/3/539
'''

can_split=False
def dfs(n,i):
    global can_split
    if can_split:
        return
    for j in range(i,n):
        if is_square(int(s[i:j+1])) and int(s[i:j+1])!=0:
            if j==n-1:
                can_split=True
                return
            dfs(n,j+1)

def is_square(x):
    if x**0.5==int(x**0.5):
        return True
    return False

s=input()
n=len(s)
dfs(n,0)
print('Yes' if can_split else 'No')