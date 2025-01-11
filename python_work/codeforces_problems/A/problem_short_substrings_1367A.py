t=int(input())
for _ in range(t):
    b=list(input())
    for i in range(1,len(b)-1):
        if i%2!=0:
            continue
        else:
            b[i]=''
    print(''.join(b))