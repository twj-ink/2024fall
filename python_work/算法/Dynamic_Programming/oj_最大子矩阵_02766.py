'''dp Kadane算法
最大子矩阵 http://cs101.openjudge.cn/practice/02766/
逐行压缩到一维数组，使用kadane算法
'''
def kanade(arr):
    max_ending_here=arr[0]
    max_sofar=arr[0]
    for i in range(1,len(arr)):
        max_ending_here=max(max_ending_here+arr[i],arr[i])
        max_sofar=max(max_ending_here,max_sofar)
    return max_sofar
def max_sum_matrix(s):
    if not s:
        return 0
    row,col=len(s),len(s[0])
    max_sum=-float('inf')

    for top in range(row):
        col_sum=[0]*col
        for bottom in range(top,row):
            for c in range(col):
                col_sum[c]+=s[bottom][c]
            max_sum=max(max_sum,kanade(col_sum))
    return max_sum

n=int(input())
nums=[]
while len(nums)<n**2:
    nums.extend(input().split())
s=[list(map(int,nums[i*n:(i+1)*n])) for i in range(n)]

max_sum=max_sum_matrix(s)
print(max_sum)