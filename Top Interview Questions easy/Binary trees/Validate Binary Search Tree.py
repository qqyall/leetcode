# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(root, low, high):
        if root.val is None:
            return True

        if root.val < high and root.val > low:
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        else:
            return False
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return helper(root, - 2^31 - 1, 2^31)
        
