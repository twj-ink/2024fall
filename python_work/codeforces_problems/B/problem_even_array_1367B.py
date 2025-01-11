t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    count_even=0
    count_odd=0
    for i in range(0,n,2):
        if nums[i]%2!=0:
            count_even+=1
    for i in range(1,n,2):
        if nums[i]%2==0:
            count_odd+=1
    if count_even==count_odd:
        print(count_odd)
    else:
        print('-1')

