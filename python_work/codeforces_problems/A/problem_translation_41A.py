s=input().strip()
t=input().strip()
list_s=list(s)
list_s.reverse()
s_re=''.join(list_s)
if s_re == t:
    print('YES')
else:
    print('NO')

s=input().strip()
t=input().strip()
if s[::-1] == t:
    print('YES')
else:
    print('NO')

#s[::-1]将字符串倒序