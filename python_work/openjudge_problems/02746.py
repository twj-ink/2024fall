def j(n,p,m):
    people=list(range(1,n+1))
    result=[]
    index=p-1
    while people:
        index=(index+m-1)%len(people)
        result.append(people.pop(index))
    return result

while True:
    n,p,m=map(int,input().split())
    if {n,m,p}=={0}:
        break
    print(','.join(map(str,j(n,p,m))))