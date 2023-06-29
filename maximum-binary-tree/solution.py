# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(ary):
            if not ary:
                return
            val = max(ary)
            index = ary.index(val)
            r = ary[index+1:]
            l = ary[:index]
            node = TreeNode(val)
            node.left = rec(l)
            node.right = rec(r)

            return node

        return rec(nums)
