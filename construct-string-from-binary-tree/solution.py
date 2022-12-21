# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = ""

        def dfs(node):
            if node is None:
                return
            self.ans += str(node.val)
            if node.left or node.right:
                self.ans += '('
                dfs(node.left)
                self.ans += ')'
                if node.right:
                    self.ans += '('
                    dfs(node.right)
                    self.ans += ')'

        dfs(root)
        return self.ans
