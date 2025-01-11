#单调栈的好处是：
#由于维护的是单调下降的高度，当弹出栈顶元素的，其左侧就是左侧第一个比它高的元素
#而弹出操作也意味着右侧就是右侧第一个比它高的元素
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        n = len(height)
        ans = 0
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                now = height[stack.pop()]
                if not stack:
                    break

                curr_h = min(height[stack[-1]], height[i])
                curr_w = i - stack[-1] - 1
                ans += (curr_h - now) * curr_w
            stack.append(i)
        return ans
if __name__ == '__main__':
    input()
    sol=Solution()
    print(sol.trap(list(map(int,input().split()))))

        # ans=0
        # stack=[]
        # for h in height:
        #     if stack and h>stack[-1]:
        #         idx=stack.index(max(stack))
        #         cut=min(h,stack[idx])
        #         for i in range(idx,len(stack)):
        #             if cut-stack[i]>0:
        #                 ans+=cut-stack[i]
        #                 stack[i]=cut
        #         # if h<stack[idx]:
        #         #     for i in range(idx+1,len(stack)):
        #         #         ans+=h-stack[i]
        #         #         stack[i]=h
        #         # else:
        #         #     for i in range(idx,len(stack)):
        #         #         ans+=stack[idx]-stack[i]
        #         #         stack[i]=stack[idx]
        #     stack.append(h)
        # return ans

        # ans = left = pre_max = suf_max = 0
        # right = len(height) - 1
        # while left < right:
        #     pre_max = max(pre_max, height[left])
        #     suf_max = max(suf_max, height[right])
        #     if pre_max < suf_max:
        #         ans += pre_max - height[left]
        #         left += 1
        #     else:
        #         ans += suf_max - height[right]
        #         right -= 1
        # return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/trapping-rain-water/solutions/1974340/zuo-liao-nbian-huan-bu-hui-yi-ge-shi-pin-ukwm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。