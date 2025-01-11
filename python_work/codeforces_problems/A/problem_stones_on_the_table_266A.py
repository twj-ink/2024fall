n=int(input())
s=input().strip()
number=0
if len(s)==1:            #
    print('0')           #
else:                    #这三行可删除
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            number+=1
    print(number)
