#week03-5.py 學習計畫 sliding Window 第4週
#LeetCode 1493.Longest Subarray of 1's After Deleting One Element
#陣列裡,一定要刪掉1個,問剩下的陣列裡,最長的1有幾個?
#sliding Window 伸縮自如的蛇,肚子裡,可以容忍最多1個0
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        zeros = 0
        tail = 0
        ans = 0
        for head in range(N):
            if nums[head]==0: zeros +=1
            while zeros > 1:
                if nums[tail]==0:zeros -=1
                tail += 1
            ans = max(ans ,head - tail +1)
        return ans-1
