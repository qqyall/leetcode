# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftSide = []
        rightSide = []
        
        def left(node):
            if node:
                leftSide.append(node.val)
                left(node.left)
                left(node.right)
            else:
                leftSide.append('null')                
        
        def right(node):
            if node:
                rightSide.append(node.val)
                right(node.right)
                right(node.left)
            else:
                rightSide.append('null')

                
        left(root)
        right(root)
        return leftSide == rightSide
        
