# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ary = []

        def dfs(node):
            if not node:
                return
            ary.append(node.val)

            dfs(node.left)
            dfs(node.right)

        def traverse(node):
            if not node:
                return

            tmp = 0
            for n in ary:
                if n > node.val:
                    tmp += n
            node.val += tmp

            traverse(node.left)
            traverse(node.right)
            return node

        dfs(root)
        return traverse(root)
