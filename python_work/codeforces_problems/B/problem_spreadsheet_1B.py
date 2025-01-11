def num_to_letter(n):
#    num=[i for i in range(0,26)]
    letter='ZABCDEFGHIJKLMNOPQRSTUVWXY'
    d,curr,ans={},[],''
#    for i in range(0,26):
#        d[num[i]]=letter[i]
    while n>26:
        a=n%26
        curr.append(d[a])
        n-=(a if a!=0 else 26)
        n//=26
        if n<=26:
            curr.append(d[n] if n!=26 else 'Z')
            break
        else:
            curr.append('Z')
    while curr:
        ans+=curr.pop()
    return ans
ntl={}
for i in range(1,10**6+1):
    ntl[i]=num_to_letter(i)
ltn={value:key for key,value in ntl.items()}

t=int(input())
for _ in range(t):
    s=input()
    if s[0]=='R' and s[1].isdigit():
        ic=s.index('C')
        num=int(s[ic+1:])
        letter=ntl[num]
        print(letter+str(s[1:ic]))
    else:
        i=0
        while not s[i].isdigit():
            i+=1
        num=ltn[s[:i]]
        print(f'R{s[i:]}C{num}')