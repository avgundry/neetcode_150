# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Val: {self.val}, Left: ({self.left}), Right: ({self.right})"

temp = ""
class Codec:
    """
    Working, but runs into out-of-memory error.
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return None
        return ','.join(self.serialize_helper(root, 0))

    def serialize_helper(self, root, i, arr=[]):
        if root == None:
            return
        while len(arr) <= i:
            arr.append("None")

        arr[i] = str(root.val)
        self.serialize_helper(root.left, 2 * i + 1, arr)
        self.serialize_helper(root.right, 2 * i + 2, arr)

        return arr
        


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        nodes = data.split(',')
        n = len(nodes)
        print(nodes)
        root = self.buildTree(0, nodes)
        return root

    def buildTree(self, i, data):
        # Builds a root from nodes i and i + 1 
        if i >= len(data) or data[i] == "None":
            return
        root = TreeNode(int(data[i]))
        root.left = self.buildTree(2 * i + 1, data)
        root.right = self.buildTree(2 * i + 2, data)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
if __name__ == "__main__":
    ser = Codec()
    deser = Codec()
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    serialized = ser.serialize(root)
    deserialized = deser.deserialize(serialized)
    print(deserialized)

    serialized2 = ser.serialize(None)
    deserialized2 = deser.deserialize(serialized2)
    print(deserialized2)
    # print(tree.left.val)
    # print(root.left.val)
    # print(c.deserialize("1,2,3,None,None,4,5"))
    # print(c.serialize(root))
    # print(c.deserialize(c.serialize(root)))