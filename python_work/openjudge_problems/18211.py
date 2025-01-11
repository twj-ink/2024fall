p=int(input())
s=sorted(list(map(int,input().split())))
n=len(s)
i,j=0,n-1
if p>=s[0]:
    while (i>=n-j-1) and i<=j:
        if p>=s[i]:
            p-=s[i]
            i+=1
        else:
            p+=s[j]
            j-=1
        if i==j:
            if p>=s[i]:
                i+=1
            else:
                break
    print(i-n+j+1)
else:
    print(0)