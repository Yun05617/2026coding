#week07-3.py 學習計畫 stack 第1題
#LeetCode 2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        ans =[]
        for c in s:
            if c=='*':ans.pop()
            else:ans.append(c)
        return ''.join(ans)
