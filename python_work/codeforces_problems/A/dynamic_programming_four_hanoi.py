'''dp
四柱汉诺塔 http://cs101.openjudge.cn/practice/01958/
用d表示三柱，f表示四柱
i柱用四柱的步骤：
1)先取i-n个利用四柱移动到某柱上，为f(i-n)
2)再将剩下的n个利用三柱移动到目标上，为d(n)
3)将i-n个移动到目标，还是f(i-n)
'''
d=[2**i-1 for i in range(13)]
f=[0]+[1]+[float('inf')]*11
for i in range(2,13):
    for j in range(1,i):
        f[i]=min(f[i],f[i-j]*2+d[j])
#print(d)
#print(f)
for i in f[1:]:
    print(i)

#an=1-2**(t-2)*(t**2-3*t-2*n+4),for t==int(sqrt(2*n))