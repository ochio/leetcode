from collections import defaultdict
from statistics import mean


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = defaultdict(list)

        def dfs(node, level):
            if node is None:
                return
            d[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        ans = []
        for k in d.keys():
            ans.append(mean(d[k]))
        return ans
