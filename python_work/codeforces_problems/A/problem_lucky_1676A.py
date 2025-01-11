t=int(input())
for _ in range(t):
#    line=list(str(input()))
#    int_line=list(map(int,line))
    int_line=list(map(int,input()))
    sum_first=sum(int_line[0:3])
    sum_last=sum(int_line[3:])
    if sum_first==sum_last:
        print('YES')
    else:
        print('NO')