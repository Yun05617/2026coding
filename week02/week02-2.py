##week02-2.py 學習計畫 Two Pointers第1題
#LeetCode 283.Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = 0
        for i in range(N):
            if nums[i] !=0:
                nums[k] = nums[i]
                k+=1
        for i in range (k,N):
            nums[i] = 0

