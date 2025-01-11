def pell(n):
    a=1;b=2
    if n==1:
        return a
    elif n==2:
        return b
    else:
        for _ in range(n-2):
            a,b=b,(2*b+a)%32767 #计算时取模减小数字，缩短时间
        return b

t=int(input())
for _ in range(t):
    n=int(input())
    print(pell(n)%32767)
#(a+b)%c=((a%c)+(b%c))%c
#(a×b)%c=((a%c)×(b%c))%c

