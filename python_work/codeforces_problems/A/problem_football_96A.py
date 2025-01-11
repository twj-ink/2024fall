s=list(map(int,input()))
n_1=0
n_0=0
for i in s:
    if i==0:
        n_0+=1
        n_1=0
        if n_0==7:
            print('YES')
            break
    else:
        n_1+=1
        n_0=0
        if n_1==7:
            print('YES')
            break
else:
    print('NO')
