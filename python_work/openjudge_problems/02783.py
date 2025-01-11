while True:
    n=int(input())
    dc=[]
    if n==0:
        break
    for _ in range(n):
        d,c=map(int,input().split())
        dc.append((d,c))
    dc.sort()
    i=j=0
    based_d_dc=[dc[0]]
    while i<n-1:
        if dc[j][1]>dc[i+1][1]:
            based_d_dc.append(dc[i+1])
            j=i+1
        i+=1
    print(len(based_d_dc))
