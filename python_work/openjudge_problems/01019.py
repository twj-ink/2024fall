#s取当前最长的12...Sk序列，因此最后只需要在这一段里面找
#判断i属于哪一段需要知道每一段的长度，使用length直接加上
#每一次更新的s的长度，就代表当前s和之前所有的s长度之和

s=''
length=0
lengths=[]

for i in range(1,40000):
    s+=str(i)
    length+=len(s)
    lengths.append(length)

t=int(input())
for _ in range(t):
    i=int(input())
    if i==1:
        print(1)
        continue
    for j in range(len(lengths)):
        if i<=lengths[j]:
            delta=i-lengths[j-1]-1
            print(s[delta])
            break
