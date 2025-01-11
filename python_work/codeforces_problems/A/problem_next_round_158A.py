n,k=map(int,input().split())
nums=list(map(int,input().split()))
advanced_nums=sum(1 for i in nums if i>=nums[k-1] and i>0)
print(advanced_nums)
