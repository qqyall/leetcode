# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = [0]
        def helper(node, k):
            if node:
                helper(node.left, k+1)
                helper(node.right, k+1)
            elif k > maxDepth[0]:
                maxDepth[0] = k

        helper(root, 0)
        return maxDepth
