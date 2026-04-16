# week08-4.py 練習計畫 Binary Search 第2題
# LeetCode 2300. Successful Pairs of Spells and Potions
# 想知道 spells[i] 魔法，配幾瓶藥水可以成功？

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # 對藥水小到大排序
        P = len(potions)  # 有 P 個藥水
        ans = []

        for spell in spells:  # 每一種魔法，都試一次
            now = P - bisect_left(potions, success / spell)
            ans.append(now)  # 全部藥水 P 瓶，會失敗的藥水有 now 瓶，便是成功的藥水數量

        return ans
