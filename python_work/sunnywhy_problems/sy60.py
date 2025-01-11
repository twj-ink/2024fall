a,b=list(map(int,input().split()))
answer=[]
for i in range(a,b+1):
    check=0
    for j in str(i):
        check+=int(j)**3
    if check==i:
        answer.append(i)
if answer:
    print(*answer)
else:
    print('NO')
