from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = deque()
        q.append(root)
        ret = []
        while q:
            qlen = len(q)
            temp = []
            for i in range(qlen):
                curr = q.popleft()
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
                temp.append(curr.val)
            ret.append(temp)
        
        return ret

        