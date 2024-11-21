# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#class Solution:
#    def hasCycle(self, head: Optional[ListNode]) -> bool:
#        pass


head = ListNode(0)
current = head
for i in range(1, 5):
    tmp = ListNode(i)
    current.next = tmp
    currnet = tmp
print()
        
