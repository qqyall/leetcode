from LinkedListClass import LinkedList


mylist = LinkedList()

for i in range(10):
    mylist.AddFirst(i)

print(mylist.count)
print(*[val.nodeValue for val in mylist.GetIterable()])


print(mylist.Insert(100000, 3))

for node in mylist.GetIterable():
    to_print = []
    for param in [node.previousNode, node, node.nextNode]:
        if param:
            to_print.append(param.nodeValue)
        else:
            to_print.append(param)
    print(*to_print)
