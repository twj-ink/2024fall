t=int(input())
def round_num(x):
    round_nums=[]
    factor=1
    while x>0:
        if x%10!=0:
            round_nums.append(x%10*factor)
        x//=10
        factor*=10
    return round_nums

for _ in range(t):
    i=int(input())
    steps=sum(1 for j in str(i) if j != '0')
    print(steps)
    print(' '.join(map(str,round_num(i))))

