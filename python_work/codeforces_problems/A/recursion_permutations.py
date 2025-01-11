'''dfs必须有退出条件
先递，再调用，再归，体现了回溯的思想
'''
curr,total=[],[]
def perm(n,curr,total):
    if len(curr)==n:
        total.append(curr.copy())
        return
    for i in range(1,n+1):
        if i in curr:
            continue

#        f=False
#        for j in curr:
#            if abs(i-j)==abs(curr.index(j)-len(curr)):
#                f=True
#        if f:
#            continue

        curr.append(i)
        perm(n,curr,total)
        curr.pop()
#八皇后
#n=int(input())
#perm(8,curr,total)
#for _ in range(n):
#    t=int(input())
#    print(''.join(map(str,total[t-1])))
n=int(input())
perm(n,curr,total)
for i in perm:
    print(*i)