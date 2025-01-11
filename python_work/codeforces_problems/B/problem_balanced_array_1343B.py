t=int(input())
for _ in range(t):
    n=int(input())
    if n%4!=0:
        print('NO')
    else:
        print('YES')
        nums1=[i for i in range(2,n+1,2)]
        sum1=sum(nums1)
        nums2=[i for i in range(1,n-2,2)]
        sum2=sum(nums2)
        m=sum1-sum2
        nums1.extend(nums2)
        nums1.append(m)

        print(' '.join(map(str,new)))
