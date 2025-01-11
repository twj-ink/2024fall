n=int(input())
s=list(map(str,input().split()))
new_s=[]
ans=[]
for i in s:
    j=i*5
    new_s.append((i,j))
new_s.sort(key=lambda x:x[1],reverse=True)
for i,j in new_s:
    ans.append(i)
print(''.join(ans),''.join(ans[::-1]))
