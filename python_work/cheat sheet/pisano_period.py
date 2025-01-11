#斐波那契数列对k取模的数列呈现pisano周期
def get_pisano_period(n,k):
    if k==1:
        return 1
    a,b,i=1,1,2
    while True:
        a,b=b,(a+b)%k
        i+=1
        if a==1 and b==0:
            return i
#如果想计算第n个能被k整除的项的index，实际上就是找摸为0
#的周期，这样只需要限制if b==0: return i即可，
#因为出现0也是有周期性的

