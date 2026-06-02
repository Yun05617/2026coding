# week14-2a.py 學習計畫 1D DP 第1題 Easy
# LeetCode 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        # 初始化 DP 陣列。前三項固定為 [0, 1, 1]，後面補上 n 個 0 確保索引不會超出範圍
        a = [0, 1, 1] + [0] * n 
        
        for i in range(3, n + 1):
            # 當前項等於前三項的總和
            a[i] = a[i-1] + a[i-2] + a[i-3]
            
        #print(a)
        return a[n]
