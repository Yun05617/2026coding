# week04-4b.py (重寫 week04-3.py)
# LeetCode 3866. First Unique Even Element
# 找到陣列 nums 裡「只出現過1次的偶數」是誰
class Solution:
    def firstUniqueEven(self, nums: List[int]) -> int:
        H = [0] * 200
        for nn in nums:  # 把陣列統計
            H[nn] += 1
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1:
                return nn
        return -1
