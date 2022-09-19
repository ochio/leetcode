# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def dfs(node, cnt):
            if node is None:
                return False
            cnt += node.val
            if node.left is None and node.right is None:
                if cnt == targetSum:
                    return True
                else:
                    return False
            return dfs(node.left, cnt) or dfs(node.right, cnt)

        return dfs(root, 0)
