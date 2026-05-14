from collections import defaultdict
from typing import List

# week12-5.py 學習計畫 Graph - DFS 第4題 Medium 題
# LeetCode 399. Evaluate Division
# 有很多分子、分母 的除法的關係
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(list)
        for (a, b), v in zip(equations, values): # 用路鏈結起來
            path[a].append((b, v)) # 正的走
            path[b].append((a, 1/v)) # 倒著走

        visited = set() # 移到外層定義，或在 helper 內共用

        def helper(now, target, v0):
            if now not in path or target not in path:
                return -1.0 # 有異常出現，不要再算！
            if now == target:
                return v0

            visited.add(now)
            for node, v in path[now]:
                if node not in visited: # 沒走過,就可以走走、試試看
                    res = helper(node, target, v0 * v)
                    if res != -1.0: # 如果找到了有效路徑，立刻回傳
                        return res
            return -1.0

        ans = []
        for a, b in queries:
            visited = set() # 每次查詢前清空走過的紀錄
            ans.append(helper(a, b, 1.0))
        return ans
