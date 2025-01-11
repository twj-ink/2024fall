def move(a,b,c,n):
    #basic case是n==1
    if n>=1:
        #先把n-1个盘子从a经过c放到b上
        move(a,c,b,n-1)
        #然后把a的剩余一个盘子(第n个盘子)放到c上
        move_one(a,c,n)
        #最后把n-1个盘子从b经过a放到c上
        move(b,a,c,n-1)

def move_one(a,c,n):
    print(f'{n}:{a}->{c}')

n,a,b,c=input().split()
n=int(n)
move(a,b,c,n)