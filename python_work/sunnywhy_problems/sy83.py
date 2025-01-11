n=int(input())
ans,ss,m='',[],float('inf')
for _ in range(n):
    s=input()
    ss.append(s)
    m=min(m,len(s))
i=0
while i<m:
    if all(ss[j][i]==ss[0][i] for j in range(1,n)):
        ans+=ss[0][i]
    else:
        break
    i+=1
print(ans)