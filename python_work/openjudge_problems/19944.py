ww={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}

n=int(input())
for _ in range(n):
    s=str(input())
    c=s[0:4];m=s[4:6];d=s[6:]

    cx=int(c);dx=int(d)
    if m =='01' or m =='02':
        m=int(m)+12
        cx-=1
    else:
        m=int(m)
    yx=int(str(cx%100))
    cx//=100

    w=(yx+yx//4+cx//4-2*cx+(26*(m+1)//10)+dx-1)%7

    print(ww[w])
