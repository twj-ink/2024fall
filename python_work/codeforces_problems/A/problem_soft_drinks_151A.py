n,k,l,c,d,p,nl,np=map(int,input().split())
a=k*l/nl
b=c*d
e=p/np
num=min(a,b,e)
real_num=num//n
print(int(real_num))
