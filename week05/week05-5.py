#week05-5.py ¾Ç²ß­pµe Hash Table(Map/Set)
#LeetCode

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        if set(counter1.keys())!=set(counter2.keys()):
            return False
        if sorted(counter1.values())!=sorted(counter2.values()):
            return False
        return True
