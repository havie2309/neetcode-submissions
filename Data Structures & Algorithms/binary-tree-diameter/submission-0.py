# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            leftdia = dfs(node.left)
            rightdia = dfs(node.right)
            diameter = max(leftdia + rightdia, diameter)
            return 1 + max(leftdia,rightdia)
        dfs(root)
        return diameter

        