#from itertools import permutations
#n=int(input())
#a=[i for i in range(1,n+1)]
#perms=sorted(permutations(a))
#for i in perms:
#    print(*i)
#from math import factorial

#n=int(input())
#a=[i for i in range(1,n+1)]
#def next_perm(a,n):
#    k=-1
#    for i in range(n-1,0,-1):
#        if a[i-1]<a[i]:
#            k=i-1
#            break
#    if k==-1:
#        return a.reverse()
#    l=-1
#    for i in range(n-1,0,-1):
#        if a[i]>a[k]:
#            l=i
#            break
#    a[l],a[k]=a[k],a[l]
#    a[k+1:]=reversed(a[k+1:])
#    return a

#print(*a)
#for i in range(factorial(n)-1):
#    print(*next_perm(a,n))
n=int(input())
chosen=[False]*(n+1)
ans=[0]*(n+1)
def dfs(k):
    if k>n:
        print(' '.join(map(str,ans[1:])))
    for i in range(1,n+1):
        if chosen[i]:
            continue
        chosen[i]=True
        ans[k]=i
        dfs(k+1)
        chosen[i]=False
dfs(1)
