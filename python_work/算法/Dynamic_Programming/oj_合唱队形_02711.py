'''dp
合唱队形 http://cs101.openjudge.cn/practice/02711/
正向的导弹拦截和逆向的导弹拦截
遍历每一个中间点，找到最多符合单调的个数
'''
n=int(input())
t=list(map(int,input().split()))
ans=float('inf')
left_dp,right_dp=[1]*n,[1]*n
for i in range(n):
    for p in range(i):
        if t[i]>t[p]:
            left_dp[i]=max(left_dp[i],left_dp[p]+1)
for j in range(n-1,-1,-1):
    for p in range(n-1,j,-1):
        if t[j]>t[p]:
            right_dp[j]=max(right_dp[j],right_dp[p]+1)
for mid in range(n):
    s=left_dp[mid]+right_dp[mid]-1
    ans=min(ans,n-s)
print(ans)