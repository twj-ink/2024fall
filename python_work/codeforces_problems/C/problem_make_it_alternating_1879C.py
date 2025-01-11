#def factorial(x):
#    if x==0 or x==1:
#        return 1
#    else:
#        return x*factorial(x-1)


from math import factorial as f

t=int(input())
for _ in range(t):
    s=list(input())
    n0=0
    n1=0
    n00=[0]
    n11=[0]
    for i in range(len(s)):
        if s[i]=='0':
            n0+=1
            if n1>=2:
                n11.append(n1)
            n1=0
        else:
            n1+=1
            if n0>=2:
                n00.append(n0)
            n0=0
    if n0>=2:
        n00.append(n0)
    if n1>=2:
        n11.append(n1)
    x1=sum(n00)+sum(n11)-len(n00)-len(n11)+2
    final_x2=[]
    x2=1
    for i in n00:
        if i!=0:
            final_x2.append(i)
    for j in n11:
        if j!=0:
            final_x2.append(j)
    for l in final_x2:
        x2*=l
    x2*=f(x1)
    print(str(x1)+' '+str(x2%998244353))

