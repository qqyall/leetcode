from LinkedListNodeClass import LinkedListNode as Node
from LinkedListClass import LinkedList


mylist = LinkedList(0)
for i in range(1, 10):
    mylist.Add(i)

n = mylist.head
k = 0 
while k < 5:
    print(n.nodeValue, n.nextNode)
    n = n.nextNode
    k += 1
