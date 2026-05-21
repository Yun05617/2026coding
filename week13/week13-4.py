#week13-4.py
from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.now = 1
        self.heap = []
        self.heap_set = set()

    def popSmallest(self) -> int:
        if self.heap:
            res = heappop(self.heap)
            self.heap_set.remove(res)
            return res

        self.now += 1
        return self.now - 1

    def addBack(self, num: int) -> None:
        # 條件：數字必須小於目前進度，且「不在」目前的堆疊中
        if num < self.now and num not in self.heap_set:
            heappush(self.heap, num)
            self.heap_set.add(num) # 標記為已在堆疊中
