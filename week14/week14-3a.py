# week14-3a.py 學習計畫 DP - 1D 第2題 Easy 題
# LeetCode 746. Min Cost Climbing Stairs
# 踩在第 i 格的梯子上，要付出 cost[i] 的代價，每次可跨 1 格 or 2 格
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache # 函式呼叫函式，把大問題，拆成小問題
        def helper(i): # 現在踩在第 i 格，之後要多少錢？
            if i >= len(cost): return 0 # 終止條件：已經爬過頂端了，不需要再付錢
            # 當前格子的花費 + min(走1格的後續花費, 走2格的後續花費)
            return cost[i] + min(helper(i+1), helper(i+2))
            
        # 可以選擇從第 0 格或第 1 格開始起跑，取兩者花費最小的
        return min(helper(0), helper(1))
