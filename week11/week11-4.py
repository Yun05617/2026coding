# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week11-4.py 學習計畫 Binary Search Tree 最後1題
# LeetCode 450. Delete Node in a BST 把某個node殺掉，再找別個頂替，放在格子裡
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root): # 找到最右邊的人
            if root.right: # 右邊還有！
                return findRightest(root.right) # 繼續往右走
            return root # 沒有右邊，那就「你」自己上

        if root == None: return root
        if root.val == key:
            # root.val = 999 # 代表要殺
            if root.left:
                now = findRightest(root.left) # 找到左邊最高的人 now
                root.val = now.val # 把準備頂替的值 填進來
                root.left = self.deleteNode(root.left, now.val) # 再把原本的人殺掉
            else:
                return root.right

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        return root
