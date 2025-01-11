s=list(map(str,input().lower()))
result=[]
n=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        n+=1
    else:
        result.append((s[i],n))
        n=1
result.append((s[-1],n))

new_result=[f'({t[0]},{t[1]})' for t in result]
print(''.join(new_result))


