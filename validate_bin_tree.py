# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def in_order_traverse_2(self, root, last_val) -> bool:
        if root.left is None:
            last_val.append(root)
        else:
            self.in_order_traverse_2(root.left, last_val)
        if root.right is None:
            last_val.append

    def in_order_traverse(self, root, last_val) -> bool:
        if root.left is not None:
            left_in_order = (root.val > root.left.val)
            if left_in_order is False:
                return False
            left_in_order = self.in_order_traverse(root.left, root.val)
            if left_in_order is False:
                return False
        if root.right is not None:
            right_in_order = (root.val < root.right.val)
            if right_in_order is False:
                return False
            right_in_order = self.in_order_traverse(root.right, root.val)
            if right_in_order is False:
                return False
        return True
        

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.in_order_traverse(root, root.val)
        