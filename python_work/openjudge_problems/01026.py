def get_cycles(n,nums):
    cycles=[]
    used=[0]*n
    for i in range(0,n):
        if used[i]:
            continue
        used[i]=1
        cycle=[i+1]
        curr=nums[i]-1
        while curr+1!=cycle[0]:
            used[curr]=1
            cycle.append(curr+1)
            curr=nums[curr]-1
        cycles.append(cycle)
    return cycles

while True:
    n=int(input())
    if n==0:
        break
    nums=list(map(int,input().split()))

    result=[]
    while True:
        line=input()
        if line=='0':
            break
        d,s=line.split(' ',1)
        d=int(d)
        ans=[' ']*n
        cycles=get_cycles(n,nums)
        for j,char in enumerate(s,1):
            for cycle in cycles:
                if j in cycle:
                    m=cycle[(cycle.index(j)+d)%len(cycle)]
                    ans[m-1]=char
                    break
        real_ans=''.join(ans)
        print(real_ans)
    print()