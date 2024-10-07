from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        elif root.val == subRoot.val:
            # Check if the ENTIRE subtree is the same.
            if self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None or root.val != subRoot.val:
            return False
        return self.isSame(root.left, subRoot.left) and \
            self.isSame(root.right, subRoot.right)
