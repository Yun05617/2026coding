# week15-1a.py 學習計畫 DP - Multidimention 第1題
# LeetCode 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(i, j):
            if i==m-1 and j==n-1: return 1
            if i==m or j==n: return 0
            return helper(i+1, j) + helper(i, j+1)
        return helper(0, 0)
