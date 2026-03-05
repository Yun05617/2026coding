#week02-5.py 學習計畫 Two Pointers 第4題 Medium
#LeetCode 1679.Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        i,j = 0,len(nums) -1
        while i <j:
            if nums[i] + nums[j] == k:
                ans +=1
                i ,j = i+1,j-1
            if nums[i] + nums[j] < k:
                i=i+1
            if nums[i]+nums[j] > k:
                j=j-1
        return ans
