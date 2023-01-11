# v1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calcHeight(root) != -1

    def calcHeight(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        left = self.calcHeight(root.left)
        right = self.calcHeight(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
