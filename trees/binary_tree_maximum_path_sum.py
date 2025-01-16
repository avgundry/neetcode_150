from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.best = -float('inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.best

    def helper(self, root):
        # At each node, we want to do two things. We want to check what the value 
        # of the path sum for the path containing the current root is,
        # and we want to return the largest path sum of the left or right paths.
        if root is None:
            # print("Returning none\n")
            return 0

        
        left = self.helper(root.left)
        # print(f"Left at root {root.val}: {left}")
        right = self.helper(root.right)
        # print(f"At root {root.val}, left = {left} and right = {right}.")
        # print(f"Previous self.best: {self.best}")

        self.best = max(self.best, max(0, left) + max(0, right) + root.val)
        # print(f"New self.best: {self.best}\n")
        return max(root.val + max(left, right), 0)
        

if __name__ == "__main__":
    s = Solution()
    # Tree1 = TreeNode(-3)
    # Tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    Tree3 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # Tree4 = TreeNode(2, TreeNode(-1))
    # Tree5 = TreeNode(-2, None, TreeNode(-3))
    # print(s.maxPathSum(Tree1))
    # print()
    # print(s.maxPathSum(Tree2))
    # print()
    print(s.maxPathSum(Tree3))
    # print()
    # print(s.maxPathSum(Tree4))
    # print()
    # print(s.maxPathSum(Tree5))
    # print()
