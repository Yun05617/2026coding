#week01-5.py 學習計畫 Array/String 第7題
#Leetcode 238. product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        preSum = [1]
        postSum = [1]
        for i in range(N):
            preSum.append( preSum[-1] * nums[i]) #每次多乘一個數
            postSum.append( postSum[-1] * nums[N-1-i])
        ans = []
        for i in range(N):
            ans.append( preSum[i] * postSum[N-1-i])
        return ans
