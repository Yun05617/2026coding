#week01-4.py 學習計畫 Array/String 第3題
#LeetCode 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #(庫存)
        ans = []
        best = max(candies)
        for candie in candies:
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False) #它會不會 >= 最多的,依序塞入 ans
        return ans

