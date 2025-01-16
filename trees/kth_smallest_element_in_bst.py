from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Super weird brute force recursion approach."""
        # Start by finding the smallest possible.
        if not root:
            return None
        curr = root
        depth = 0
        while curr.left:
            depth += 1
            curr = root.left
        # Curr is now the smallest node...hmmm. :\ 
        if k == 0:
            return root


        

        