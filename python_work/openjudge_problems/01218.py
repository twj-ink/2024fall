t=int(input())
for _ in range(t):
    n=int(input())
    s=[0]*n
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j%i==0:
                s[j-1]+=1
    for i in range(n):
        if s[i]%2==0:
            s[i]=0
        else:
            s[i]=1
    print(sum(s))