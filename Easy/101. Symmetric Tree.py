# v1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSymmetricBinary(l: Optional[TreeNode],
                              r: Optional[TreeNode]) -> bool:
            if not l and not r:
                return True
            elif not l or not r:
                return False
            return l.val == r.val \
                and isSymmetricBinary(l.left, r.right) \
                and isSymmetricBinary(l.right, r.left)

        return isSymmetricBinary(root.left, root.right)
