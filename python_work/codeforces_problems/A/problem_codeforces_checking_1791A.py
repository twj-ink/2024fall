t=int(input())
a='codeforces'
a_list=list(a)
for _ in range(t):
    w=input()
    if w in a_list:
        print('YES')
    else:
        print('NO')