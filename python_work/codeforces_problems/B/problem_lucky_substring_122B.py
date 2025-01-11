def is_luckydigits(x):
    return x=='4' or x=='7'
n=input()
check=sum(1 for i in n if is_luckydigits(i))
if check==0:
    print('-1')
else:
    cnt4=n.count('4')
    cnt7=n.count('7')
    print(['4','7'][cnt4<cnt7])
