# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        next_nodes = [root]
        res = []
        while next_nodes != []:
            cur_nodes = next_nodes.copy()
            next_nodes = []
            arr = []
            for cnode in cur_nodes:
                if cnode is not None:
                    arr.append(cnode.val)
                    next_nodes.append(cnode.left)
                    next_nodes.append(cnode.right)
            if len(arr) != 0:
                res.append(arr)
        return res
