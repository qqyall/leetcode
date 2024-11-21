from LinkedListNodeClass import LinkedListNode as Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def Add(self, newNode: int):
        addingNode = Node(newNode)

        if self.head == None:
            self.head = addingNode
            self.tail = addingNode
        else:
            self.tail.nextNode = addingNode
            self.tail = addingNode
        self._count += 1

    def Insert(self, item, pos):
        if pos > self.count - 1 or pos < 0:
            return False

        addingNode = Node(item)
        
        if pos == 0:
            addingNode.nextNode = self._head
            self._head = addingNode
        elif pos == self.count - 1:
            self.Add(item)
        else:    
            k = 0
            currentNode = self._head
            while k < pos - 1:
                currentNode = currentNode.nextNode
                k += 1
            nextNode = currentNode.nextNode
            
            addingNode.nextNode = nextNode
            
            currentNode.nextNode = addingNode

        self._count += 1
        return True
        
    def GetLength(self):
        return self._count

    def Remove(self, item):
        previousNode = None
        currentNode = self._head

        # 1: Пустой список: ничего не делать.
        # 2: Один элемент: установить Previous = None.
        # 3: Несколько элементов:
        #    a: Удаляемый элемент первый.
        #    b: Удаляемый элемент в середине или конце.      
        while(currentNode != None):
            if (currentNode.nodeValue == item):

                # Узел в середине или в конце.
                if previousNode:

                    # Случай 3b.
                    # До:    Head -> 3 -> 5 -> None
                    # После: Head -> 3 ------> None                 
                    previousNode.nextNode = currentNode.nextNode

                    # Если в конце, то меняем _tail.
                    if currentNode.nextNode == None:
                        self._tail = previousNode
                        
                else:
                    # Случай 2 или 3a.

                    # До:    Head -> 3 -> 5
                    # После: Head ------> 5

                    # Head -> 3 -> null
                    # Head ------> null                  
                    self._head = self.head.nextNode

                    # Список теперь пустой? 
                    if self._head == None:
                        self._tail = None

                self._count -= 1
                return True
            
            previousNode = currentNode
            currentNode = currentNode.nextNode
        return False

            
    def Clear(self):
        self._head = None
        self._tail = None
        self._count = 0


    def GetIterable(self):
        currentNode = self._head

        while currentNode:
            yield currentNode.nodeValue
            currentNode = currentNode.nextNode


    def Contains(self, item):
        for nodeValue in self.GetIterable():
            if nodeValue == item:
                return True
        return False
    
   
    def CopyTo(self, array, arrayIndex=0):
        for nodeValue in self.GetIterable():
            array[arrayIndex] = nodeValue
            arrayIndex += 1
        
        
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, newHead):
        self._head = newHead

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, newTail):
        self._tail = newTail

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
