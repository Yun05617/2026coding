#week07-6.py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0 # 目前被消滅的次數，都還是 0
        R, D = senate.count('R'), senate.count('D') # 目前各別有幾個人？

        while queue: # 只要還有人在排隊，就繼續進行「互相 Ban 對方」遊戲
            now = queue.popleft() # 左邊吐出個字母，它要消滅「敵對陣營」
            if now == 'R':
                if banR > 0: # 已經記錄要消滅 1 個人
                    banR -= 1 # 用掉 1 個消滅的名額
                    R -= 1 # 馬上少掉 1 個人
                    # 這裡被消滅了，不 append 回去
                else: # 你沒有被消滅，太好了，你可以反過來消滅對方
                    banD += 1
                    queue.append(now) # 再到最右邊排隊
            else: # now == 'D'
                if banD > 0:
                    banD -= 1
                    D -= 1
                    # 這裡被消滅了，不 append 回去
                else:
                    banR += 1
                    queue.append(now)

            # 只要有一方人歸零，遊戲就結束
            if R == 0: return 'Dire' # 把 R 消滅光，'D' 就得勝
            if D == 0: return 'Radiant' # 把 D 消滅光，'R' 就得勝

        return ""
