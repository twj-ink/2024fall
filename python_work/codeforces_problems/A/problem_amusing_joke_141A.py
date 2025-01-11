a=list(input())
b=list(input())
c=list(input())
total=a+b
if sorted(total)==sorted(c):
    print('YES')
else:
    print('NO')