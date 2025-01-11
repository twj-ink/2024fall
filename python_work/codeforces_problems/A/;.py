for _ in range(int(input())):
    n,k=map(int,input().split())
    events=[]
    for i in list(map(int,input().split())):
        events.append((i,1)) #表示下一个价格这个事件将变为bad
    for i in list(map(int,input().split())):
        events.append((i,2)) #表示下一个价格这个事件将变为无评价
    events.sort()
    i=0
    cost=0
    bad=0
    people=n
    while i<n*2:
        curr=events[i][0]
        if bad<=k:
            cost=max(cost,people*events[i][0])
        while i<n*2 and events[i][0]==curr:
            bad+=(events[i][1]==1)
            bad-=(events[i][1]==2)
            people-=(events[i][1]==2)
            i+=1
    print(cost)




