from math import ceil

while True:
    n=int(input())
    vt=[]
    ts=[]
    if n==0:
        break
    for _ in range(n):
        v,t=map(int,input().split('\t'))
        if t>=0:
            v/=3.6
            vt.append((v,t))
    vt.sort(key=lambda x:x[1])
    for i,(v,t) in enumerate(vt):
        t1=ceil((4500/vt[0][0])+vt[0][1])
        ts.append(t1)
        if ceil((4500/vt[i][0])+vt[i][1]) <=t1:
            ti=ceil((4500/vt[i][0])+vt[i][1])
            ts.append(ti)

    print(min(ts))
