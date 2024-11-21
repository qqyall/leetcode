from LinkedListNodeClass import LinkedListNode as Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def AddLast(self, newNode: int):
        addingNode = Node(newNode)

        if self.head == None:
            self.head = addingNode
            self.tail = addingNode
        else:
            tmp = self.tail
            self.tail.nextNode = addingNode
            self.tail = addingNode
            self.tail.previousNode = tmp
        self._count += 1

    def AddFirst(self, newNode: int):
        addingNode = Node(newNode)

        if self.head == None:
            self.head = addingNode
            self.tail = addingNode
        else:
            tmp = self.head
            self.head = addingNode
            self.head.nextNode = tmp
            tmp.previousNode = self.head
        self._count += 1

    def Insert(self, item, pos):
        if pos > self.count - 1 or pos < 0:
            return False

        addingNode = Node(item)
        
        if pos == 0:
            self.head.previousNode = addingNode
            addingNode.nextNode = self._head
            self._head = addingNode
        elif pos == self.count - 1:
            self.AddLast(item)
        else:    
            k = 0
            for node in self.GetIterable():
                if k == pos:
                    tmp = node
                    prevNode = tmp.previousNode
                    prevNode.nextNode = addingNode
                
                    node = addingNode
                    node.previousNode = prevNode
                    node.nextNode = tmp

                    tmp.previousNode = node
                    k+=1
                else:
                    k+=1

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

            # Head -> 3 -> 5 -> 7 -> null
            # Head -> 3 ------> 7 -> null
            if (currentNode.nodeValue == item):

                # Узел в середине или в конце.
                if previousNode:

                    # Случай 3b.
                    previousNode.nextNode = currentNode.nextNode
                    
                    # Если в конце, то меняем _tail.
                    if currentNode.nextNode == None:
                        self._tail = previousNode
                        
                else:
                    # До:    Head -> 3  5  7 -> null
                    # После: Head -> 3  7 -> null

                    # previousNode = 3
                    # currentNode = 5
                    # current.nextNode = 7
                    # Значит... 7.Previous = 3
               
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
            yield currentNode
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
