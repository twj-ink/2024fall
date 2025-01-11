#n个石子，两人轮流拿，一次拿1-m个
#谁最后一个将石头拿完谁赢
def last_zero_win(n,m):
    if n%(m+1)==0:
        return '先手必输'
    else:
        return '先手必赢'

#谁最后一个将石头拿完谁输
def last_zero_lose(n,m):
    dp=[False]*(n+1)
    for i in range(2,n+1):
        dp[i]=(True if any(dp[i-j]==False for j in range(1,m+1)) else False)
