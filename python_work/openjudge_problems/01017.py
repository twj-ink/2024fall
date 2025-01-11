while True:
    a,b,c,d,e,f=map(int,input().split())
    if a==b==c==d==e==f==0:
        break
    cnt=f
    while e>0:
        cnt+=1
        e-=1
        if a<=11:
            a=0
        else:
            a-=11
    while d>0:
        cnt+=1
        d-=1
        if b<=5:
            if a:
                if a<=20-4*b:
                    a=0
                else:
                    a-=(20-4*b)
            b=0
        else:
            b-=5
    if c>0:
        cnt+=c//4
        c%=4
        if c==0:
            c=0
        elif c==1:
            cnt+=1
            if b<=5:
                if a<=27-b*4:
                    a=0
                else:
                    a-=27-b*4
                b=0
            else:
                b-=5
                if a<=7:
                    a=0
                else:
                    a-=7
        elif c==2:
            cnt+=1
            if b<=3:
                if a<=18-4*b:
                    a=0
                else:
                    a-=18-4*b
                b=0
            else:
                b-=3
                if a<=6:
                    a=0
                else:
                    a-=6
        elif c==3:
            cnt+=1
            if b<=1:
                if a<=9-4*b:
                    a=0
                else:
                    a-=9-4*b
                b=0
            else:
                b-=1
                if a<=5:
                    a=0
                else:
                    a-=5
    if b>0:
        cnt+=b//9
        b%=9
        if b==0:
            b=0
        else:
            cnt+=1
            if b==1:
                if a<=32:
                    a=0
                else:
                    a-=32
            elif b==2:
                if a<=28:
                    a=0
                else:
                    a-=28
            elif b==3:
                if a<=24:
                    a=0
                else:
                    a-=24
            elif b==4:
                if a<=20:
                    a=0
                else:
                    a-=20
            elif b==5:
                if a<=16:
                    a=0
                else:
                    a-=16
            elif b==6:
                if a<=12:
                    a=0
                else:
                    a-=12
            elif b==7:
                if a<=8:
                    a=0
                else:
                    a-=8
            elif b==8:
                if a<=4:
                    a=0
                else:
                    a-=4
    if a>0:
        cnt+=a//36
        a%=36
        if a>0:
            cnt+=1
    print(cnt)