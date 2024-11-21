class LinkedListNode:
    def __init__(self, value: int):
        self.__nodeValue = value
        self.__nextNode = None

    @property
    def nodeValue(self):
        return self.__nodeValue

    @nodeValue.setter
    def nodeValue(self, value):
        self.__nodeValue = value

    @property
    def nextNode(self):
        return self.__nextNode
    
    @nextNode.setter
    def nextNode(self, node):
        self.__nextNode = node

