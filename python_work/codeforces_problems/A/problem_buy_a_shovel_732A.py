k,r=map(int,input().split())
if k%10==0:
    print('1')
else:
    i=1
    while i <10:
        if k*i%10==0:
            break
        elif (k*i%10) !=r:
            i+=1
        else:
            break
    print(i)
