# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        if root:
            self.root.val = 0
        self.s = set()

        def dfs(node):
            if not node:
                return
            self.s.add(node.val)

            if node.left:
                node.left.val = 2 * node.val + 1
                dfs(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                dfs(node.right)

        dfs(self.root)

    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
