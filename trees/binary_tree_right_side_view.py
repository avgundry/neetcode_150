import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # OH, I see. This problem is just kinda poorly explained.
        if not root:
            return []
        res = []
        dq = collections.deque()
        dq.append(root)
        while dq:
            n = len(dq)
            for i in range(n):
                curr = dq.popleft()
                if curr.left != None:
                    dq.append(curr.left)
                if curr.right != None:
                    dq.append(curr.right)
            # Will contain the rightmost node's val at the end.
            res.append(curr.val)

        return res
        