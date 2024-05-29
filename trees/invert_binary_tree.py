from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Runtime-optimal solution"""
        if root == None:
            return None
        l = None
        r = None
        if root.left != None:
            l = self.invertTree(root.left)
        if root.right != None:
            r = self.invertTree(root.right)
        root.left = r
        root.right = l

        return root

        """Memory-optimal solution"""
        # if root == None:
        #     return None

        # temp = root.right
        # root.right = self.invertTree(root.left)
        # root.left = self.invertTree(temp)

        # return root

        