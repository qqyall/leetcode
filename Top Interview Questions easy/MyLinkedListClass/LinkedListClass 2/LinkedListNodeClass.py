class LinkedListNode:
    def __init__(self, value):
        self._nodeValue = value
        self._nextNode = None
        self._previousNode = None
        
        
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
    
    @property
    def previousNode(self):
        return self._previousNode

    @previousNode.setter
    def previousNode(self, new_previousNode):
        self._previousNode = new_previousNode
