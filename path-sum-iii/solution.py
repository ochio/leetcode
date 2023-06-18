# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def dfs(node, comb):
            if not node:
                return
            c = comb+[node.val]
            for i in range(len(c)):
                if sum(c[i:]) == targetSum:
                    self.count += 1

            dfs(node.left, c)
            dfs(node.right, c)

        dfs(root, [])
        return self.count
