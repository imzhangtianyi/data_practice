class TreeNode:
    def __init__(self, x):
        """
        initialize a tree node
        :param x: value of the node
        """
        self.val = x
        self.left = None
        self.right = None


class BST:
    def _add(self, node, x):
        """
        add node
        :param x: value of node
        :return: node
        """
        if not node:
            return TreeNode(x)
        if node.val >= x:
            node.left = self._add(node.left, x)
        else:
            node.right = self._add(node.right, x)
        return node

    def inorder(self, root):
        stack = []
        arr = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            arr.append(node.val)
            node = node.right
        return arr


if __name__ == "__main__":
    root = None
    for i in [1, 2, 5, 4, 3]:
        root = BST()._add(root, i)

    print(BST().inorder(root))
