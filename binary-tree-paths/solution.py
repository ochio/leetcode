# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        s = []

        def dfs(root, path):
            if root is None:
                return
            if path is None:
                path = str(root.val)
            else:
                path = path + '->' + str(root.val)

            if root.left is None and root.right is None:
                s.append(path)

            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root, None)
        return s
