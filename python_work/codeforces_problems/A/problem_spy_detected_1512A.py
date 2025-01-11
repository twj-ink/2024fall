t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    if nums[0]!=nums[1] and nums[1]==nums[2]:
        print(1)
    elif nums[-1]!=nums[-2] and nums[-2]==nums[-3]:
        print(len(nums))
    else:
        for i in range(1,n-1):
            if nums[i-1]!=nums[i] and nums[i]!=nums[i+1]:
                print(i+1)
