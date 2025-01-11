#MLE
import sys
maxn=10**8
memo=[0]*(maxn+1)
for n in range(1,maxn+1):
    if n==1:
        memo[n]=1
    elif n==2:
        memo[n]=1
    elif n==3:
        memo[n]=2
    elif n==4:
        memo[n]=3
    elif n%4==0 and n!=4:
        memo[n]=memo[(n-2)//2-1]+(n-2)//2+1
    elif (n-2)%4==0:
        memo[n]=memo[n//2-1]+n//2
    else:
        memo[n] = memo[n-1]+1
data=sys.stdin.readlines()
t=int(data[0].strip())
result=[]
for i in range(1,t+1):
    n=int(data[i].strip())
    result.append(memo[n])
sys.stdout.write('\n'.join(map(str,result))+'\n')
#TLE
import sys
data=sys.stdin.readlines()
t=int(data[0].strip())
memo={}
for i in range(1,t+1):
    n=int(data[i].strip())
    nn=n
    cnt=0
    while n>0:
        if n in memo:
            cnt+=memo[n]
            break
        if n%4==0 and n!=4:
            cnt+=1
            n-=2
            cnt+=n//2
            n=n//2-1
        elif n==4:
            cnt+=3
            n=0
        elif (n-2)%4==0:
            cnt+=n//2
            n=n//2-1
        else:
            cnt+=1
            n-=1
            if n==0:
                break
            if n==4:
                cnt+=1
                break
            if n % 4 == 0:
                n-=1
                cnt+=1;n-=1
                n//=2
            elif (n-2)%4==0:
                n//=2
    print(cnt)
    if nn not in memo:
        memo[nn]=cnt