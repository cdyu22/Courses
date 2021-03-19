class Linked_List:

    class __Node:

        def __init__(self, val):
            self.value = val
            self.next = None #The new node starts out pointing nowhere.
            self.previous = None

    def __init__(self):
        self.__header = Linked_List.__Node(None) #Only nodes containing no value
        self.__tailer = Linked_List.__Node(None)
        self.__header.next = self.__tailer #Point the sentinels to each other
        self.__tailer.previous = self.__header
        self.__size = 0

    def __len__(self): #Constant Time
        return self.__size

    def append_element(self, val): #Constant Time
        newest = Linked_List.__Node(val)
        newest.next = self.__tailer
        newest.previous = self.__tailer.previous
        self.__tailer.previous.next = newest
        self.__tailer.previous = newest #Now in 'tail' position.
        self.__size += 1

    def insert_element_at(self, val, index): #Linear Time
        if index >= self.__size or index < 0:
            raise IndexError
        newest = Linked_List.__Node(val)

        if index < self.__size/2: #Decides to walk forward or backward
            current = self.__header
            #Walk current to the node before insertion point
            for i in range(index):
                current = current.next
            newest.next = current.next
            newest.previous = current
            current.next = newest
            newest.next.previous = newest
        else:
            current = self.__tailer
            #Walk to node after insertion point
            for i in range(self.__size-index):
                current = current.previous
            newest.next = current
            newest.previous = current.previous
            current.previous.next = newest
            current.previous = newest

        self.__size += 1

    def remove_element_at(self, index): #Linear Time
        if index >= self.__size or index < 0:
            raise IndexError

        if index < self.__size/2: #Forwards
            current = self.__header
            for i in range(index+1): #Walk to the node.
                current = current.next
            current.next.previous = current.previous
            current.previous.next = current.next
        else: #Backwards
            current = self.__tailer
            for i in range(self.__size-index): #Walk to the node.
                current = current.previous
            current.next.previous = current.previous
            current.previous.next = current.next

        self.__size -= 1
        return current.value

    def get_element_at(self, index): #Linear Time
        if index >= self.__size or index < 0:
            raise IndexError

        if index < self.__size/2: #Decides if forwards or backwards.
            current = self.__header
            for i in range(index+1):
                current = current.next
        else:
            current = self.__tailer
            for i in range(self.__size-index):
                current = current.previous

        return current.value

    def rotate_left(self): #Constant Time
        if len(self) < 1:
            return
        current = self.__header.next
        value = current.value
        current.next.previous = current.previous
        current.previous.next = current.next
        newest = self.__Node(value)
        newest.next = self.__tailer
        newest.previous = self.__tailer.previous
        self.__tailer.previous.next = newest
        self.__tailer.previous = newest

    def __str__(self): #Linear Time
        if self.__size == 0:
            return '[ ]'
        #Have to do this, or else printing an empty linked list will
        #print a bracket with two spaces.
        string = [None] * self.__size
        current = self.__header
        for i in range(self.__size):
            current = current.next
            string[i] = str(current.value)
        string = ', '.join(string)
        return '[ ' + string + ' ]'

    def __iter__(self): #Constant Time
        self.keeper = 0 #Keeps track of values
        return self

    def __next__(self): #Constant Time, but for loop works in linear time
        if self.keeper == self.__size:
            raise StopIteration
        current = self.__header.next.value
        self.rotate_left() #Will eventually rotate back to original position
        self.keeper += 1
        return current

if __name__ == '__main__':

#------------------------------append_element-----------------------------
    print("Testing append_element")
    append_test = Linked_List()

    #Testing if it can add a node to an empty list.
    append_test.append_element(4)
    print(append_test)

    #Testing if it places the node in the 'tail' position.
    append_test.append_element(5)
    append_test.append_element(6)
    print(append_test)

    #Testing if it can append 0 or negative numbers to the linked list.
    append_test.append_element(0)
    append_test.append_element(-521)
    print(append_test)

    #Testing if it can add other classes into the linked list.
    append_test.append_element(5.0)
    append_test.append_element('Value')
    append_test.append_element([1,2,3])
    print(append_test)

#---------------------------insert_element_at-----------------------------
    print("\nTesting insert_element_at")
    insert_test = Linked_List()

    #Testing if it can insert a node into an empty list.
    try:
        insert_test.insert_element_at(0,0)
    except IndexError:
        print("Error: Cannot insert into empty list")

    for i in range(5):
        insert_test.append_element(i)
    print(insert_test)

    #Testing if the method can add a node into an already populated list.
    insert_test.insert_element_at(-1,3)
    print(insert_test)

    #Testing if it correctly cannot insert node into the 'tail' position.
    try:
        insert_test.insert_element_at(10,6)
    except IndexError:
        print("Error: Cannot insert node into tail position")

    #Testing if it correctly cannot insert a node past the end of the list.
    try:
        insert_test.insert_element_at(0,7)
        print(insert_test)
    except IndexError:
        print("Error: Cannot insert element past end of list")

    #Testing negative indexing
    print(insert_test)
    try:
        insert_test.insert_element_at(0,-1)
    except IndexError:
        print("Error: Cannot insert into a negative index")
    print(insert_test) #Didn't change the structure or length of the list.

#---------------------------remove_element_at-------------------------------
    print("\nTesting remove_element_at")
    test3 = Linked_List()

    #Testing remove on an empty list.
    try:
        test3.remove_element_at(0)
    except IndexError:
        print("Error: No Nodes")

    #Testing if it can remove nodes from the list.
    for i in range(10):
        test3.append_element(i)
    print(test3)
    test3.remove_element_at(0)
    test3.remove_element_at(4)
    test3.remove_element_at(7)
    print(test3) #Successfully removes

    #Trying to remove with negative indexing
    try:
        test3.remove_element_at(-1)
    except IndexError:
        print("Error: Negative Indexing")
        print(test3)

    #Trying to remove past end of linked list
    try:
        test3.remove_element_at(10)
    except IndexError:
        print("Error: Index out of list")
        print(test3)

#--------------------------------__len__-----------------------------------
    print("\nTesting __len__")
    len_test = Linked_List()
    print("Linked List has " + str(len(len_test)) + " Values")

    for i in range(10):
        len_test.append_element(i)
    print("Linked List has " + str(len(len_test)) + " Values")

    #Testing len with all modifying methods
    len_test.append_element(0)
    print("Linked List has " + str(len(len_test)) + " Values")
    len_test.insert_element_at(5,0)
    print("Linked List has " + str(len(len_test)) + " Values")
    len_test.remove_element_at(5)
    print("Linked List has " + str(len(len_test)) + " Values")

    #Testing if errors still modify list or length
    print(len_test)
    try:
        #Should not modify
        len_test.insert_element_at(0,-1)
    except IndexError:
        print("Error: Negative Indexing")
        print("Linked list remains unchanged")
        print(len_test)
    try:
        #Should not modify
        len_test.remove_element_at(-1)
    except IndexError:
        print("Error: Negative Indexing")
        print("Linked list remains unchanged")
        print(len_test)

#-----------------------------get_element_at-------------------------------
    print("\nTesting get_element_at")
    get_test = Linked_List()
    for i in range(10):
        get_test.append_element(i)
    print(get_test)
    print(get_test.get_element_at(0))
    print(get_test.get_element_at(4))
    print(get_test.get_element_at(9))

    #Testing negative indexing
    try:
        get_test.get_element_at(-1)
    except IndexError:
        print("Error: Negative Indexing")

    #Trying to get value from a node that's past the end of the linked list.
    try:
        get_test.get_element_at(10)
    except IndexError:
        print("Error: Index Out of Range")
    print(get_test)
    print(len(get_test))

#------------------------------rotate_left---------------------------------
    print("\nTesting rotate_left")
    rotate_test = Linked_List()

    #Trying to rotate empty list
    try:
        rotate_test.rotate_left()
    except IndexError:
        print("Error: Cannot Rotate an Empty List")

    #Trying to rotate list
    for i in range(10):
        rotate_test.append_element(i)
    print(rotate_test)
    rotate_test.rotate_left()
    print(rotate_test) #Works

#-----------------------------------__str__---------------------------------
    print("\nTesting __str__")
    str_test = Linked_List()

    #Printing empty list
    print(str_test)

    #Printing short list
    for i in range(10):
        str_test.append_element(i)
    print(str_test)

    #Printing long list
    for k in range(100):
        str_test.append_element(k)
    print(str_test)

#-----------------------------------for loop---------------------------------
    print("\nTesting for loop")
    test7 = Linked_List()
    for i in range(100,0,-10):
        test7.append_element(i)

    #Testing if it reaches retrieves every value in every node.
    for val in test7:
        print(val)
