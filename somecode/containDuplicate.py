class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BST(object):
    def __init__(self):
        self.t = float('inf')

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        self.t = t
        self.root = None

        for indx, val in enumerate(nums):
            if indx - 1 >= k:
                self.root = self._delete(self.root, nums[indx - k - 1])
            self.root, res = self._add(self.root, val)
            if res:
                return res
        return False

    def _delete(self, node, val):
        if not node:
            return None
        if node.val > val:
            return
            # node.left = self._delete(node.left, val)
        elif node.val < val:
            return
            # node.right = self._delete(node.right, val)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right

            tmp_node = node.right
            tmp_val = node.right.val
            while tmp_node.left:
                tmp_node = tmp_node.left
                tmp_val = tmp_node.val

            node.val = tmp_val
            node.right = self._delete(node.right, tmp_val)
            return node

    def _add(self, node, val):
        if not node:
            return TreeNode(val), False
        res = self._check(node, val)
        if res:
            return node, True
        if node.val > val:
            node.left, res = self._add(node.left, val)
        elif node.val <= val:
            node.right, res = self._add(node.right, val)
        return node, res

    def _check(self, node, val):
        res = False
        if abs(node.val - val) <= self.t:
            res = True
        return res


if __name__ == "__main__":
    ans = BST().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 2)
    print(ans)
