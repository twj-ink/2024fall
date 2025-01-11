n,m,a=map(int,input().split())
nums=[]
for i in [n,m]:
    if i%a==0:
        n_needed=int(i/a)
    else:
        n_needed=int(i//a+1)
    nums.append(n_needed)
print(int(nums[0]*nums[1]))
