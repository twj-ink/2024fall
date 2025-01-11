def move(n,a='A',b='B',c='C'):
    if n>=1:
        move(n-1,f'{a}',f'{c}',f'{b}')
        move_one(a,c)
        move(n-1,f'{b}',f'{a}',f'{c}')
def move_one(a,c):
    print(f'{a}->{c}')

n=int(input())
print(2**n-1)
move(n)