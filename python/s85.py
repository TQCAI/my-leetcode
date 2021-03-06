from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        left = [0] * N
        right = [N] * N
        stack = []
        for i in range(N):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        return max(heights[i] * (right[i] - left[i] - 1) for i in range(N))

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if not N:
            return 0
        M = len(matrix[0])
        if not M:
            return 0
        heights = [0] * M
        ans = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans