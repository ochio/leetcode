# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.left and node.left.val == target:
                if node.left.left is None and node.left.right is None:
                    node.left = None
            if node.right and node.right.val == target:
                if node.right.left is None and node.right.right is None:
                    node.right = None

        dfs(root)
        if root.val == target and root.left is None and root.right is None:
            return None
        return root
