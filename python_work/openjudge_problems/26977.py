# from typing import List
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans=0
#         stack=[]
#         for h in height:
#             if stack and h>stack[-1]:
#                 idx=stack.index(max(stack))
#                 cut=min(h,stack[idx])
#                 for i in range(idx,len(stack)):
#                     if cut-stack[i]>0:
#                         ans+=cut-stack[i]
#                         stack[i]=cut
#                 # if h<stack[idx]:
#                 #     for i in range(idx+1,len(stack)):
#                 #         ans+=h-stack[i]
#                 #         stack[i]=h
#                 # else:
#                 #     for i in range(idx,len(stack)):
#                 #         ans+=stack[idx]-stack[i]
#                 #         stack[i]=stack[idx]
#             stack.append(h)
#         return ans
# if __name__ == '__main__':
#     n=int(input())
#     sol=Solution()
#     print(sol.trap(list(map(int,input().split()))))

def trap(height):
    ans=0
    stack=[]
    i=0
    while i<len(height):
        while stack and height[i]>height[stack[-1]]:
            h=height[stack.pop()]
            if not stack:
                break
            distance=i-stack[-1]-1
            ans+=distance*(min(h,))
