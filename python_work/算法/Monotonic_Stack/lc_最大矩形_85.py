from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m, ans = len(matrix), len(matrix[0]), 0
        prefix = [[0] * (m + 2) for _ in range(n + 2)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = 0 if matrix[i-1][j-1] == '0' else prefix[i - 1][j] + 1

        for i in range(1, n + 1):
            stack = [0]
            ans_ = 0
            for j in range(1, n + 1):
                while stack and prefix[i][j] < prefix[i][stack[-1]]:
                    curr_h = prefix[i][stack.pop()]
                    curr_w = j - stack[-1] - 1
                    ans_ = max(ans_, curr_h * curr_w)
                stack.append(j)
            ans = max(ans, ans_)
        return ans
if __name__ == '__main__':
    sol=Solution()
    print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))