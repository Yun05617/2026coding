#week05-3.py 厩策璸礶 Hash Table (Map/Set)
#LeetCode 1207. Unique Number of Occurrences
#–贺计,瞷Ω计ゲ斗常ぃ妓
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s = set()
        for c in counter:
            if counter[c] in s:
                return False
            s.add(counter[c])
        return True
