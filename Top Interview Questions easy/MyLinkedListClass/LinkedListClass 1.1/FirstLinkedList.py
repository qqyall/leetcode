from LinkedListClass import LinkedList


mylist = LinkedList()

for i in range(10):
    mylist.Add(i)

print(mylist.count)

mylist.Remove(0)
mylist.Remove(5)
mylist.Remove(9)

print([val for val in mylist.GetIterable()])

print(mylist.GetLength())

print(mylist.Contains(5), mylist.Contains(9))

lst = [_ for _ in range(11, 22)]

mylist.CopyTo(lst, 1)
print(lst)

mylist.Clear()
print('mylist =', [val for val in mylist.GetIterable()])

for i in range(10):
    mylist.Add(i)
print(mylist.Insert(100,5))
print('mylist =', [val for val in mylist.GetIterable()])


