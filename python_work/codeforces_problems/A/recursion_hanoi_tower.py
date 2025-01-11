'''dfs必须有结束条件
汉诺塔 http://cs101.openjudge.cn/practice/04147
只需明确设置函数的作用：将n个盘子从a通过b拿到c
最少2**n-1次
'''
def move(n,a,b,c):
    if n>=1:
        move(n-1,a,c,b)
        move_one(n,a,c)
        move(n-1,b,a,c)

def move_one(n,a,c):
    print(f'{n}:{a}->{c}')

move(6,'A','B','C')
