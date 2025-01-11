def is_luckydigit(x):
    return x=='4' or x=='7'
def is_luckynum(x):
    return all(is_luckydigit(i) for i in str(x))
def next_lucky(x):
    y=str(x)
    z=''
    for i in y:
        if int(i)<=4 or int(i)>7:
            z+='4'
        else:
            z+='7'
    return int(z)

l,r=map(int,input().split())
s=[]
for i in range(l,r+1):
    s.append(next_lucky(i))
print(sum(s))


