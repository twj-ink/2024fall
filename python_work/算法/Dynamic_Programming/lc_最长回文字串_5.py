#dp[i][j]表示从i到j的子列是否是回文的
def longestPalindrome(s):
    max_len=0
    start=0
    n=len(s)
    if n==1:
        return s
    dp=[[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i]=1
    #滑动窗口
    for L in range(2,n+1):
        for i in range(n):
            j=i+L-1
            if j>=n:
                break
            if s[i]==s[j]:
                if j-i<3:
                    #如果长度是1或者2
                    dp[i][j]=1
                else:
                    #向内部找字串的dp值
                    dp[i][j]=dp[i+1][j-1]
            #循环内部直接维护最大值
            if dp[i][j] and j-i+1>max_len:
                max_len=j-i+1
                start=i
    return s[start:start+max_len]
