class LinkedListNode:
    def __init__(self, value):
        self._nodeValue = value
        self._nextNode = None

    @property
    def nodeValue(self):
        return self._nodeValue

    @nodeValue.setter
    def nodeValue(self, new_value):
        self._nodeValue = new_value

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, new_nextNode):
        self._nextNode = new_nextNode
    

