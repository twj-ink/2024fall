a,b,c=map(int,input().split())
num=0
answer=[]

for sx in range(1,82):
    x=b*(sx**a)+c
    y=x
    digits=[]
    if y<10:
        digits.append(y)
    else:
        while y//10!=0:
            digits.append(y%10)
            y//=10
            if y<10:
                digits.append(y)
                break

    if sum(digits)==sx:
        num+=1
        answer.append(x)
    digits.clear()
print(num)
print(' '.join(map(str,answer)))