from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.best = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return max(self.best - 1, 0)

    def helper(self, root: Optional[TreeNode]):
        if not root:
            return 0
        # depth of left tree + depth of right tree
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.best = max(self.best, l + r + 1)
        # return the max depth of this subtree
        return 1 + max(l, r)
        