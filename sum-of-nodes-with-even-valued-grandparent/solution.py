# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(node, parents):
            if not node:
                return 0
            cnt = 0
            if len(parents) < 2:
                dfs(node.left, parents + [node.val])
                dfs(node.right, parents + [node.val])
            else:
                if parents[-2] % 2 == 0:
                    cnt += node.val

            return cnt + dfs(node.left, parents + [node.val]) + dfs(node.right, parents + [node.val])

        return dfs(root, [])
