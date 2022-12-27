from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d = defaultdict(int)

        stack = [root]
        ans = False

        while stack:
            node = stack.pop()
            v = k - node.val
            if d[v]:
                ans = True
                break
            else:
                d[node.val] = 1
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

        return ans
