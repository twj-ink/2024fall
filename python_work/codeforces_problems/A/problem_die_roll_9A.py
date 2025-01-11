import math

y,m=map(int,input().split())
t=sum(1 for i in range(max(y,m),7))
total=6
d=math.gcd(t,total)
d_t=t//d  #用//相当于直接取整
d_total=total//d
print(str(d_t)+'/'+str(d_total))
