n,m=map(int,input().split())
nums=list(map(int,input().split()))
new_nums=[]
for _ in range(m):
    i=min(nums)
    if i<=0:
        new_nums.append(i)
        nums.remove(i)
print(abs(sum(new_nums)))


n,m=map(int,input().split())
nums=list(map(int,input().split()))
new_nums=[]
for i in nums:
    if i<=0:
        new_nums.append(i)
j=min(m,len(new_nums))
new_nums.sort()
money=abs(sum(new_nums[:j]))
print(money)


n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
ans=0
i=0
while i<=m-1:
    if a[i]<=0:
        ans+=a[i]
        i+=1
    else:
        break
print(-ans)
