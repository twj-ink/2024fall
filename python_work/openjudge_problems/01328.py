from math import sqrt
turn=0
while True:
    turn+=1
    n,d=map(int,input().split())
    can_cover,f=[],False
    if {n,d}=={0}:
        break
    for _ in range(n):
        x,y=map(int,input().split())
        if y>d:
            f=True
        else:
            right=x+sqrt(d**2-y**2)
            left=x-sqrt(d**2-y**2)
            can_cover.append([left,right])
    if f==True:
        print(f'Case {turn}: -1')
        input()
        continue
    can_cover.sort(key=lambda x:x[1])
    cnt,mark=0,-float('inf')
    for coverage in can_cover:
        if coverage[0]>mark:
            cnt+=1
            mark=coverage[1]
    print(f'Case {turn}: {cnt}')
    input()
