import sys
input=lambda: sys.stdin.readline()

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cnt,i,j,curr=0,0,0,0
    while j<n and i<n:
        if a[i]>0:
            while j<n and a[j]>0:
                curr=0
                curr=max(curr,a[j])
                j+=1
            cnt+=curr
            i=j
        else:
            while j<n and a[j]<0:
                curr=-float('inf')
                curr=max(curr,a[j])
                j+=1
                print(curr)
            cnt+=curr
            i=j
    print(cnt)