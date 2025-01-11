from math import factorial

def get_next_permutation(a):
    #从后往前遍历找到第一个降序的数字的index
    #a[k-1]<a[k],get this k
    n=len(a)
    k=-1
    for i in range(n-1,0,-1):
        if a[i-1]<a[i]:
            k=i-1
            break
    if k==-1:
        a.reverse()
        return a
    #从后往前找到大于这个数字的索引最大值
    #a[l]=a[k]+1
    l=-1
    for i in range(n-1,k,-1):
        if a[i]>a[k]:
            l=i
            break
    #互换二者位置
    a[l],a[k]=a[k],a[l]
    #将a[k+1]到末尾的所有数字反转
    a[k+1:]=reversed(a[k+1:])
    return a
m=int(input())
for _ in range(m):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if n==1:
        print(*a)
    else:
        for i in range(k%factorial(len(a))):
            a=get_next_permutation(a)
        print(*a)