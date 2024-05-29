from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Iterative solution"""
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        best = 0
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                best = max(best, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return best



    """Recursive solution"""
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root == None:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))