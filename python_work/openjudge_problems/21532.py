#n=int(input())
#i=6
#while n%i!=0:
#    i+=1
#print(n//i)

#from math import gcd
#current=0
#n=int(input())
#for a in range(1,n):
#    for b in range(a+1,n):
#        if a==b:
#            continue
#        for c in range(b+1,n):
#            if a+b+c!=n:
#                continue
#            if c==a or c==b:
#                continue
#            x=gcd(a,b);y=gcd(x,c)
#            current=max(current,y)
#print(current)

n=int(input())
for i in range(n//3,0,-1):
    if n%i!=0:
        continue
    else:
        if n//i<6:
            continue
        else:
            print(i)
            break