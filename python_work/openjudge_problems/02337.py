t=int(input())
for _ in range(t):
    a=''
    n=int(input())
    s=[input() for _ in range(n)]
    for i in range(n-1):
        if s[i][-1]==s[i+1][0]:
            a+=s[i]+'.'

        else:
            a='***'
            break
    if  a!='***' and s[-2][-1]==s[-1][0]:
        a+=s[-1]
    else:
        a='***'
    print(a)