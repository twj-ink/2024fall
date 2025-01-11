'''dp起始条件的填充
拦截导弹 http://cs101.openjudge.cn/practice/02945/
Dilworth_theory 使用二分查找
最长不升子序列->反转得到最长不降子序列(longest non_decreasing sequence)
'''
#dp
n=int(input())
s=list(map(int,input().split()))
dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        if s[i]<=s[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))

#Dilworth_theory
from bisect import bisect_right

def min_tester_needed(s):
    s.reverse()
    lnds=[]
    for i in s:
        pos=bisect_right(s,i)
        if pos<len(lnds):
            lnds[pos]=i
        else:
            lnds.append(i)
    return len(lnds)

n=int(input())
s=list(map(int,input().split()))
result=min_tester_needed(s)
print(result)

