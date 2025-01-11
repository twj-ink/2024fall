#t=int(input())
#for _ in range(t):
#    n,k=map(int,input().split())
#    a=list(map(int,input().split()))
#    new_a=sorted(a[:])
#    b=sorted(list(map(int,input().split())))
#    new_b=[]
#    for i in new_a:
#        for j in b:
#            if abs(i-j)<=k:
#                new_b.append(j)
#                b.remove(j)
#                break
#    print(' '.join(map(str,new_b)))

#保存a的各个数据位置，可以采用(a[i],i)的元组形式保存在一个列表中
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    indexed_a=sorted((a[i],i) for i in range(n))
    result=[0]*n
    j=0
    for ai,original_index in indexed_a:
        while j<n and abs(ai-b[j])>k:
            j+=1
        if j<n:
            result[original_index]=b[j]
            j+=1
    print(' '.join(map(str,result)))


