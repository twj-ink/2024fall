from math import sqrt

n=int(input())
for _ in range(n):
    a,b,c=map(float,input().split())
    if b*b-4*a*c>0:
        x1=(-b+sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-sqrt(b*b-4*a*c))/(2*a)
        print('x1='+str('%.5f'% x1)+';x2='+str('%.5f'% x2))
    elif b*b-4*a*c==0:
        if -b/(2*a)!=0:
            print('x1=x2='+str('%.5f'% (-b/(2*a))))
        else:
            print('x1=x2=0.00000')
    else:
        p=str('%.5f'% (-b/(2*a)))
        q=str('%.5f'% (sqrt(-(b*b-4*a*c))/(2*a)))
        if -b/(2*a)!=0:
            print('x1='+p+'+'+q+'i;x2='+p+'-'+q+'i')
        else:
            print('x1=0.00000+'+q+'i;x2=0.00000-'+q+'i')
