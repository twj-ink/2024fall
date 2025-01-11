def min_needed(r,position):
    position=sorted(position)
    n=len(position)
    cnt=0
    i=0

    while i<n:
        #mark -> the position to place the stone
        mark=i
        while mark<n and position[mark]<=position[i]+r:
            mark+=1
        #place the stone at position[mark]-1
        cnt+=1
        i=mark-1
        #continue to cover more place
        while i<n and position[i]<=position[mark-1]+r:
            i+=1
    return cnt

while True:
    r,n=map(int,input().split())
    if {r,n}=={-1}:
        break
    position=list(map(int,input().split()))
    cnt=min_needed(r,position)
    print(cnt)