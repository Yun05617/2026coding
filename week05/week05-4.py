#week05-4.py
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row)for row in grid])

        preSum = 0
        for row in grid:
            preSum += sum(row)
            if preSum == total - preSum:
                return True
        preSum = 0
        for col in zip(*grid):
            preSum += sum(col)
            if preSum == total - preSum:
                return True
        return False
