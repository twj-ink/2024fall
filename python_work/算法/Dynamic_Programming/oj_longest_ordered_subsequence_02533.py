from bisect import bisect_left
def lis(n,a):
    dp=[]
    for num in a:
        pos=bisect_left(dp,num)
        if pos==len(dp):
            dp.append(num)
        else:
            dp[pos]=num
    return len(dp)
n=int(input())
a=list(map(int,input().split()))
print(lis(n,a))
