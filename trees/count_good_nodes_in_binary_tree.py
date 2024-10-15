# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.recurse(root, float('-inf'))

    def recurse(self, root, highest):
        """
        Recursively counts good nodes, keeping track of the highest
        value seen in the tree so far.
        """
        if root == None:
            return 0
        new_highest = max(highest, root.val)
        return (highest <= root.val) + self.recurse(root.left, new_highest) \
            + self.recurse(root.right, new_highest)

if __name__ == "__main__":
    s = Solution()
    tree = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print(s.goodNodes(tree))
        
        