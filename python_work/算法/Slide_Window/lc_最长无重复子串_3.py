#双指针，右指针向右遍历，左指针跟着走，每次检查新元素是否已经出现
#若已经出现要把左指针挪到重复元素右边，再更新长度
#O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        left=0
        window=set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            L=max(L,len(window))
        return L