# v1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        lst_node_residual = [(root, targetSum - root.val)]
        while lst_node_residual:
            node, residual = lst_node_residual.pop()
            if (residual == 0) and not node.left and not node.right:
                return True
            if node.left:
                lst_node_residual.append((node.left, residual - node.left.val))
            if node.right:
                lst_node_residual.append(
                    (node.right, residual - node.right.val)
                )
        return False
