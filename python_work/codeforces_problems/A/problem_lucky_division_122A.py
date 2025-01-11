def is_luckydigits(x):
    return x=='4' or x=='7'
def is_luckynum(x):
    return all(is_luckydigits(i) for i in str(x))
s=[x for x in range(4,778) if is_luckynum(x)]
n=int(input())
for i in s:
    if n%i==0:
        print('YES')
        break
else:
    print('NO')