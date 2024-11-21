from LinkedListNodeClass import LinkedListNode as Node


class LinkedList:
    def __init__(self, node):
        self.__head = Node(node)
        self.__tail = Node(node)
        self.__count = 1

    def Add(self, item):
        new_node = Node(item)
        
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.__nextNode = new_node
            self.__tail = new_node
        self.__count+=1
        

    def Remove(item: int):
        pass

    def Contains(item: int):
        pass

    @property
    def head(self):
        return self.__head 

    @head.setter
    def head(self, head):
        self.__head  = head
    
    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, tail):
        self.__tail  = tail
    
    @property
    def count(self):
        return self.__count 

    @count.setter
    def count(self, count):
        self.__count  = count


