#对于每一个柱子，找到左边第一个高度小于其的柱子
#和右边第一个高度小于其的柱子
#这就是以该柱子为高度的最宽矩形
##边界添加0和0，保证最后剩余和相等的有解
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[0]
        n=len(heights)
        heights=[0]+heights+[0]
        ans=0

        for i in range(1,n+2):
            while stack and heights[i]<heights[stack[-1]]:
                curr_h=heights[stack.pop()]
                curr_w=i-stack[-1]-1
                ans=max(ans,curr_h*curr_w)
            stack.append(i)
        return ans
if __name__ == '__main__':
    sol=Solution()
    print(sol.largestRectangleArea([3,1,3,2,2]))