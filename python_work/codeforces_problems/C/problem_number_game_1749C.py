from math import ceil
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    maxk=ceil(n/2)
    #从最大数向下遍历
    for k in range(maxk,0,-1):
        f=True
        aa=a[:]
        #模拟过程
        for i in range(1,k+1):
            #找到A可取的最大数字，没找到就寄
            found=False
            for val in aa[::-1]:
                if val<=k-i+1:
                    aa.pop(aa.index(val))
                    found=True
                    break
            if not found:
                f=False
                break
            #B把最小的移除
            if aa:
                aa.append(aa.pop(0)+k-i+1)
        if f:
            print(k)
            break
    else:
        print(0)

