
def split_pile(n,ans):
    if n not in ans:
        ans.add(n)
    if n%3==0:
        split_pile(n//3,ans)
        split_pile((n//3)*2,ans)
    return ans
t=int(input())
used={}
for _ in range(t):
    n,m=map(int,input().split())
    if n in used:
        ans=used[n]
    else:
        ans=split_pile(n,set())
        used[n]=ans
    if m in ans:
        print('YES')
    else:
        print('NO')