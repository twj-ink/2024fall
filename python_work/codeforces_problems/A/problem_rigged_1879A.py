t=int(input())
for _ in range(t):
    n=int(input())
    s_and_e=[]
    new=[]
    for _ in range(n):
        s,e=map(int,input().split())
        s_and_e.append((s,e))
    for i in range(1,n):
        if s_and_e[i][1]>=s_and_e[0][1]:
            new.append(s_and_e[i])
    if new:
        m=max(i[0] for i in new)
        if s_and_e[0][0]>m:
            print(m+1)
        else:
            print(-1)
    else:
        print(s_and_e[0][0])