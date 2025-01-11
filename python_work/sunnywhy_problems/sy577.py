s=input()
i=1
ans=[]
for j in range(0,len(s)-1):
    if s[j]!=s[j+1]:
        i+=1
    else:
        ans.append(i)
        i=1
ans.append(i)
print(max(ans))