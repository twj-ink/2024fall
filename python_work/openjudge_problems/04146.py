n=int(input())
ans=[]
for a in range(n,-1,-1):
    for b in range(n,-1,-1):
        if (a+b)%2!=0:
            continue
        for c in range(n,-1,-1):
            if (b+c)%3!=0 or (a+b+c)%5!=0:
                continue
            else:
                ans.append((a+b+c))
print(max(ans))

