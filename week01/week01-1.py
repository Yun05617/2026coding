#week01-1
#LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to one
# 案计 //2, 计+1, 拜或跑1
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0 #羆璶ǐ碭˙
        n = int (s,2)#р﹃ s 讽窽俱计跑 n
        while n > 1:#ヘ夹:n程跑Θ1
            if n%2==0: n = n // 2 #案计//2
            else: n = n +1 #计+1
            ans += 1 #暗˙!
        return ans #羆惠璶ǐ碭˙
