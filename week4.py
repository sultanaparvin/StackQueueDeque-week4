class listItem:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self, data):
        newitem = listItem(data, None, self.head)
        self.head = newitem
        if self.tail is None: # Was empty, so tail points to the same as the head now
            self.tail = newitem
        if newitem.next is not None: # Set the previous head to reference new item as its previous
            newitem.next.prev = newitem

    def push_back(self, data):
        newitem = listItem(data, self.tail, None)
        self.tail = newitem
        if self.head is None: # Was empty, so head points the new tail too
            self.head = newitem
        if newitem.prev is not None: # Set the next reference of the previous tail to the new item
            newitem.prev.next = newitem


    def pop_front(self):
        if self.head is None: # None if empty
            return None
        frontitem = self.head
        self.head = frontitem.next
        if self.head is not None: # check if the new head exists, not empty list
            self.head.prev = None # Set the new head previous reference to None
        else:
            self.tail = None # if removed the last element, set tail to None as well
        return frontitem.data

    def pop_back(self):
        if self.tail is None: # Return None if empty
            return None
        tailitem = self.tail 
        self.tail = tailitem.prev
        if self.tail is not None: # check if the new tail exists, i.e non-empty list still
            self.tail.next = None # Set the new tail next reference to None
        else:
            self.head = None  # If removed last tail element, list is empty, set head to None
        return tailitem.data

class Stack:
    def __init__(self):
        self.storage = Deque()
    
    def push(self, data):
        self.storage.push_back(data)
    
    def pop(self):
        return self.storage.pop_back()


class Queue:
    def __init__(self):
        self.storage = Deque()
    
    def push(self, data):
        self.storage.push_back(data)
    
    def pop(self):
        return self.storage.pop_front()

        


tst = Queue()
for i in range(10):
    tst.push(i)
    
while True:
    data = tst.pop()
    if data is None:
        break
    print(data)

tst = Stack()
for i in range(30, 40):
    tst.push(i)
    
while True:
    data = tst.pop()
    if data is None:
        break
    print(data)
