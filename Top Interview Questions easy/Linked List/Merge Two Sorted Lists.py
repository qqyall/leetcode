# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        tmp = list1
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next
        tmp = list2
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next

        nums = sorted(nums)
        if (len(nums)) == 0:
            return None
        head = ListNode(nums[0])
        currentNode = head
        for i in range(1, len(nums)):
            tmp = ListNode(nums[i])
            currentNode.next = tmp
            currentNode = currentNode.next
        currentNode.next = None
        return head
