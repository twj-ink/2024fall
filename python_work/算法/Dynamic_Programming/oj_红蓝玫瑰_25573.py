'''dp
红蓝玫瑰 http://cs101.openjudge.cn/practice/25573/
建立两个dp，分别为全变为红色的操作数和全变为蓝色的操作数
'''
s=input()
n=len(s)
dpr=[0]*n
dpb=[0]*n
if s[0]=='R':
    dpr[0],dpb[0]=0,1
else:
    dpr[0],dpb[0]=1,0
for i in range(1,n):
    if s[i]=='R':
        dpr[i]=dpr[i-1]
        dpb[i]=min(dpr[i-1],dpb[i-1])+1
    else:
        dpr[i]=min(dpr[i-1],dpb[i-1])+1
        dpb[i]=dpb[i-1]
print(dpr[-1])