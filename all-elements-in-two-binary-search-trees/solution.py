# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ary = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            ary.append(node.val)
            dfs(node.right)

        dfs(root1)
        dfs(root2)

        ary.sort()
        return ary
