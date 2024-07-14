# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Brute force"""
        pPath = self.dfs(root, p, [])
        qPath = self.dfs(root, q, [])

        # print("pPath:")
        # for node in pPath:
        #     print(node)
        #     print()

        # print("\n\nqPath:")
        # for node in qPath:
        #     print(node)
        #     print()

        # reduce so both are same length of depth
        if len(pPath) > len(qPath):
            pPath = pPath[:len(qPath)]
        if len(qPath) > len(pPath):
            qPath = qPath[:len(pPath)]

        while pPath[-1] != qPath[-1]:
            pPath.pop()
            qPath.pop()

        return pPath[-1]


        

    def dfs(self, root, target, visited):
        if root == None:
            return []
        elif root.val == target.val:
            return visited + [root]
        else:
            left = self.dfs(root.left, target, visited + [root])
            right = self.dfs(root.right, target, visited + [root])
            if left == [] and right == []:
                return []
            elif left != []:
                return left
            else:
                return right
        