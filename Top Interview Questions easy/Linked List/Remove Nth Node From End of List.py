# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        currentNode = head

        while currentNode.next != None:
            currentNode = currentNode.next
            length += 1
            
        currentNode = head
        if length == 1:
            return
        if n == 1:
            for i in range(length - 2):
                currentNode = currentNode.next
            currentNode.next = None
            return head
        
        for i in range(length - n):
            currentNode = currentNode.next

        nextNode = currentNode.next
        currentNode.val =  nextNode.val
        currentNode.next = nextNode.next

        return head
