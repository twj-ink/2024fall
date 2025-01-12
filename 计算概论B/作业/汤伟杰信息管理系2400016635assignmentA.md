# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>汤伟杰，信息管理系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：

​	斐波那契数列，使用空间复杂度低的方法来写。如果需要取模的话要在(a+b)后就取模。

代码：

```python
def step(n):
    if n==1 or n==2:
        return n
    a,b=1,2
    for _ in range(n-2):
        a,b=b,a+b
    return b

print(step(int(input())))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126151055772](C:/Users/ink/AppData/Roaming/Typora/typora-user-images/image-20241126151055772.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：

​	是第一题的进阶，上一题只与前两个状态有关，这个题与之前的所有状态都有关，但是要加上直接一步上完楼梯的1步。

代码：

```python
def step(n):
    if n==1 or n==2:
        return n
    dp=[1,2]+[0]*(n-2)
    for i in range(2,n):
        dp[i]=1+sum(dp[j] for j in range(i))
    return dp[-1]

print(step(int(input())))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241126151607069](C:/Users/ink/AppData/Roaming/Typora/typora-user-images/image-20241126151607069.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：

​	见第二段代码的关键式子：dp[i]=dp[i-1]+dp[i-k]，借助了gpt帮助才理解：对第i个长度，可以选择在第i-1个长度末尾加一个R，或者选择在第i-k个长度末尾加一组W。这时候我才发现和作业前两题的关系。。写的第一段代码感觉逻辑有点不对但是答案是对的，问gpt也不太理解？

代码：

```python
#只构建前缀和数组，dp数组用第一题的小空间来存储
mod=10**9+7
t,k=map(int,input().split())
prefix=[1]+[0]*(10**5)
for i in range(1,10**5+1):
    if i<k:
        prefix[i]=i+1
    else:
        last=1
        curr=last+prefix[i-k]
        prefix[i]=(prefix[i-1]+curr)%mod
        last=curr%mod
 
for _ in range(t):
    a,b=map(int,input().split())
    print((prefix[b]-prefix[a-1])%mod)
    
#构建dp数组和前缀和数组
mod=10**9+7
t,k=map(int,input().split())
dp=[1]+[0]*(10**5)
prefix=[0]+[0]*(10**5)
for i in range(1,10**5+1):
    if i<k:
        dp[i]=1
    else:
        dp[i]=(dp[i-1]+dp[i-k])
        dp[i]%=mod
for i in range(1,10**5+1):
    prefix[i]=(prefix[i-1]+dp[i])%mod
 
for _ in range(t):
    a,b=map(int,input().split())
    print((prefix[b]-prefix[a-1])%mod)
```



代码运行截图 <mark>（至少包含有"Accepted"）4000KB是代码1，8200KB是代码2</mark>

![image-20241127101038926](C:/Users/ink/AppData/Roaming/Typora/typora-user-images/image-20241127101038926.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：

​	我自己想到的是中心扩展的思路，结果代码写的又臭又长且debug了半天。思路是遍历两次，第一次是中心点是一个字符，然后把每一个中心点对应的回文长度记录在字典d1里；第二次是中心点是两个字符，同理记录 在d2里。由于可能不存在以2个字符为中心的，所以要初始化d2为{0:0}防止后续取最大值的时候报错了。

​	看到了题解代码好简单，主要的点是注意到中心点不管是1还是2，只要中心满足回文串，只需要查看向两边扩散的两个字符是否相等即可，这比我用切片和其reverse之后的比较要简洁；同时只遍历一次，每遍历一个就记录以该字符为1或2中心的最大长度，然后使用start和end不断维护。好简洁。。。同时学习了dp的写法，自己没想到，题解应该有滑动窗口从小到大的感觉。

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return ''.join(s)
        if n==2:
            return (''.join(s) if s[0]==s[1] else s[0])

        d1={};d2={0:0}
        for i in range(1,n-1):
            half=1
            while i-half>=0 and i+half<=n-1 and s[i-half:i+half+1][::-1]==s[i-half:i+half+1]:
                half+=1
            d1[i]=2*(half-1)+1

        for i in range(n-1):
            if s[i]==s[i+1]:
                half=1
                while i-half>=0 and i+1+half<=n-1 and s[i-half:i+1+half+1][::-1]==s[i-half:i+1+half+1]:
                    half+=1
                d2[i]=2*(half-1)+2

        index1=max(d1,key=d1.get)
        length1=d1[index1]
        index2=max(d2,key=d2.get)
        length2=d2[index2]
        if length1>length2:
            half=(length1-1)//2
            return ''.join(s[index1-half:index1+half+1])
        half=(length2-2)//2
        return ''.join(s[index2-half:index2+1+half+1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126233446364](C:/Users/ink/AppData/Roaming/Typora/typora-user-images/image-20241126233446364.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：

​	输入输出是gpt写的，自己写的一直re；bfs内容是看群里同学的代码和问gpt写的，后来一直MLE；最后看老师的题解找不同找半天，发现一个更新的写法不同导致空间复杂度差距巨大，这我自己肯定是写不出来的。

代码：

```python
from collections import deque
import sys
input=sys.stdin.read
dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(s,x,y,i,j,water,m,n):
    q=deque([(x,y,s[x][y])])
    water[x][y]=s[x][y]
    while q:
        x,y,height=q.popleft()
        for _ in range(4):
            nx,ny=x+dx[_],y+dy[_]
            if 0<=nx<m and 0<=ny<n and s[nx][ny]<height and water[nx][ny]<height:
                water[nx][ny]=height   #####如果写成water[nx][ny]=s[x][y]会MLE
                q.append((nx, ny,height))
def main():
    data=input().split()
    idx = 0
    k = int(data[idx])
    idx += 1
    result = []
    for _ in range(k):
        m, n = map(int, data[idx:idx+2])
        idx += 2
        #矩阵
        s = [list(map(int, data[idx+i*n:idx+(i+1)*n])) for i in range(m)]
        idx += m * n
        #司令部
        i, j = map(int, data[idx:idx+2])
        i-=1;j-=1
        idx += 2
        p = int(data[idx])
        idx += 1
        water=[[0]*n for _ in range(m)]
        #起点
        for _ in range(p):
            x,y=map(int,data[idx:idx+2])
            idx+=2
            x-=1;y-=1
            if s[x][y]<=s[i][j]:
                continue
            bfs(s,x,y,i,j,water,m,n)
        if water[i][j]>0:
            result.append('Yes')
        else:
            result.append('No')
    sys.stdout.write('\n'.join(result) + '\n')
if __name__ == '__main__':
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241128150411230](C:/Users/ink/AppData/Roaming/Typora/typora-user-images/image-20241128150411230.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：

​	本题笨人做了1天，最后对着答案改了1个小时。。。。坑点：

①横纵坐标互换，读入n和m要换位置，x1,y1,x2,y2也要换位置

②因为终点不是空格，所以始终不可能保存到duque里面，因此在for循环内部要随时查看几个方向是否到达终点，如果到达就把线段添加的答案列表里面，再继续遍历其他方向，这也是为什么if s[nx] [ny]==' ':的判断语句后置的原因，同时也是因为这不是求最小步数

③所有的线段要全部保存，最后取最小值（但是我自己想不到）

④deque保存的不仅仅是点的坐标，由于不能回溯所以要把当前这个点的方向状态和线段数状态以参数的形式向前传递

⑤最后要print()

代码：

```python
from collections import deque
dx,dy=[0,-1,1,0],[-1,0,0,1]
def bfs(x1,y1,seg,dir,segs):
    q=deque()
    q.append((x1,y1,seg,dir))
    inq=set()
    inq.add((x1,y1,dir))
    while q:
        for _ in range(len(q)):
            x,y,seg,dir=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n+2 and 0<=ny<m+2 and (nx,ny,i) not in inq:
                    new_seg=seg+(1 if dir!=i else 0)
                    new_dir=i
                    if (nx,ny)==(x2,y2):
                        segs.append(new_seg)
                        continue
                    if s[nx][ny]==' ':
                        q.append((nx,ny,new_seg,new_dir))
                        inq.add((nx,ny,i))
    if segs:
        return min(segs)
    else:
        return False

idx=0
while True:
    idx+=1
    m,n=map(int,input().split())
    if {m,n}=={0}:
        break
    s=[' '*(m+2)]+[' '+input()+' ' for _ in range(n)]+[' '*(m+2)]
    print(f'Board #{idx}:')
    a=[]
    i=0
    while True:
        i+=1
        y1,x1,y2,x2=map(int,input().split())
        if {x1,x2,y1,y2}=={0}:
            break
        ans=bfs(x1,y1,0,-1,[])
        if ans:
            print(f'Pair {i}: {ans} segments.')
        else:
            print(f'Pair {i}: impossible.')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![bd121178530d2366c8ff6c614138a2ea](C:/Users/ink/Documents/Tencent%20Files/298731943/nt_qq/nt_data/Pic/2024-11/Ori/bd121178530d2366c8ff6c614138a2ea.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

​	回文子串数据是10**3，因此完全可以二重循环，有可能就是要二维dp数组，感觉这个有引导作用？

​	Flowers想到了数学方法用组合数去做，但是由于要用factorial函数，数据太大了导致时间复杂度不允许，不知道有没有优化方法![image-20241128151231678](C:/Users/ink/AppData/Roaming/Typora/typora-user-images/image-20241128151231678.png)

​	后两题好难啊而且是模板变形，花了我1天又3/4左右的时间吧，群里同学怎么做到的几个小时啊😭

![image-20241128150449162](C:/Users/ink/AppData/Roaming/Typora/typora-user-images/image-20241128150449162.png)
