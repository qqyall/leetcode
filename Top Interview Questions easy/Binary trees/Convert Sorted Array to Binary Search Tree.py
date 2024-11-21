# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        f(nums, 0 , len(nums) - 1)

        
    def f(arr, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2        

        tmpNode = TreeNoed(arr[mid])

        tmpNode.left = f(arr, left, mid - 1)
        tmpNode.right = f(arr, mid + 1, right)

        return tmpNode
