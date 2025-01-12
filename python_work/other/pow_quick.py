#内置的pow很快，mth.pow输出浮点数，直接输出整数
#下面是快速幂
#若exp%2==0，则base**exp=(base**2)**(exp//2)
###指数减半，底数平方########
def quick_pow(base,exp,mod):
    result=1
    while exp>0:
        if exp%2==1:
            result=result*base%mod
        base=base*base%mod
        exp//=2
    return result

print(pow(2,1000000000000,10**9+7))
print(quick_pow(2,1000000000000,10**9+7))
# print((2**1000000000000)%10**9+7) 很慢！！