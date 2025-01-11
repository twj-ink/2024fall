n,t=map(int,input().split())
s=list(input())
for _ in range(t):
    i=0
    while i < len(s)-1:
        if s[i]=='B' and s[i+1]=='G':
            s[i],s[i+1]=s[i+1],s[i]
            i+=1
        i+=1
print(''.join(s))

