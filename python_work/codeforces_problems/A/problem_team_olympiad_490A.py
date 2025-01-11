def team_olympiad(n,a):
    pg=[]
    ms=[]
    pe=[]
    for i in range(n):
        if a[i]==1:
            pg.append(i+1)
        elif a[i]==2:
            ms.append(i+1)
        else:
            pe.append(i+1)
    w=min(len(pg),len(ms),len(pe))
    print(w)
    for i in range(w):
        print(pg[i],ms[i],pe[i])

n=int(input())
a=list(map(int,input().split()))
team_olympiad(n,a)