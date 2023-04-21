# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(s, e):
            if s > e:
                return [None]
            if s == e:
                return [TreeNode(s)]

            result = []
            for i in range(s, e+1):
                left = dfs(s, i-1)
                right = dfs(i+1, e)

                for l in left:
                    for r in right:
                        tmp = TreeNode(i)
                        tmp.left = l
                        tmp.right = r
                        result.append(tmp)
            return result
        return dfs(1, n)
