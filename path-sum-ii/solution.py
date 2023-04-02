# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        a = []

        def dfs(node, comb):
            if not node:
                return
            if not node.left and not node.right:
                if sum(comb + [node.val]) == targetSum:
                    a.append(comb + [node.val])
                return

            if node.left:
                dfs(node.left, comb + [node.val])
            if node.right:
                dfs(node.right, comb + [node.val])

        dfs(root, [])
        return a
