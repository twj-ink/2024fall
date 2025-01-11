n=int(input())
s=[]
cnt=2
for _ in range(n):
    x,h=map(int,input().split())
    s.append([x,h])
#如果只有1棵树显然只能fall一个
if n==1:
    print(1)
else:
    mark=s[0][0]
    for i in range(1,n-1):
        #与前一棵树之间有空位
        if s[i][0]-mark>s[i][1]:
            cnt+=1
            mark=s[i][0]
        #如果不行看与后一棵树的空位
        elif s[i+1][0]-s[i][0]>s[i][1]:
            cnt+=1
            mark=s[i][0]+s[i][1]
        #如果都不能要把mark更新到当前的树
        else:
            mark=s[i][0]
    print(cnt)