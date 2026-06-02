# week14-3b.py 學習計畫 DP - 1D 第2題 Easy 題
# LeetCode 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        a = [0] * (N + 1) # 用來查表的表格

        a[0] = cost[0]
        a[1] = cost[1] # 幸好題目規格「一定有2格」

        for i in range(2, N + 1):
            # 挑選從前一格 (i-1) 或前兩格 (i-2) 走過來的最小累積花費
            a[i] = min(a[i-1], a[i-2])

            # 如果還沒超過樓梯頂端，就必須加上踩在當前格子 cost[i] 的代價
            if i < N:
                a[i] += cost[i]

        return a[N]
