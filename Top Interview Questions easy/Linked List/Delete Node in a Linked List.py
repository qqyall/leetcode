# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #node - нода, куторую надо удалить, а не целый связный список

        #получаем следующую за удаляемой нодой ноду
        nextNode = node.next

        #записываем значение следущей ноды в значение удаляемой ноды
        #то есть на самом деле мы не удаляем ноду, а переписываем её 
        #на следующую ноду
        node.val = nextNode.val

        #в параметр next ноды вписываем значение next слудующей ноды
        node.next = nextNode.next

        #в итоге мы не удалили ноду, а записали на ее место следующую ноду
        #забавно, но я думал, что тогда надо написать в параметр next
        #предыдущей ноды значение следующей ноды, но мы этого не делаем
