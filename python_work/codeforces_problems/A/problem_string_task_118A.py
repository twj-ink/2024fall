s=list(input().lower())
for i in ['a','o','y','e','u','i']:
    while i in s:
        s.remove(i)
for i in s:
    print('.'+i,end='')
