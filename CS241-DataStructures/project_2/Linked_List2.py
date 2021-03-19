class Linked_List:

  class __Node:

    def __init__(self, val):
        self.value = val
        self.next = None
        self.previous = None

  def __init__(self):
      self.header = self.__Node(None)
      self.tailer = self.__Node(None)
      self.header.next = self.tailer
      self.tailer.previous = self.header
      self.__size = 0

  def __len__(self):
      return self.__size

  def append_element(self, val):
      newest = self.__Node(val)
      newest.next = self.tailer
      newest.previous = self.tailer.previous
      self.tailer.previous.next = newest
      self.tailer.previous = newest
      self.__size += 1

  def insert_element_at(self, val, index):
      if index >= self.__size:
          raise IndexError
      newest = self.__Node(val)
      cur = self.header
      for i in range(index):
          cur = cur.next
      newest.next = cur.next
      cur.next = newest
      newest.next.previous = newest
      newest.previous = cur
      self.__size += 1 #CAN WE INSERT THINGS AT INDEX 0?

  def remove_element_at(self, index):
      if index >= self.__size:
          raise IndexError
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored
    # in the node at the specified index. If the index
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node
    # at the specified index, but do not unlink it from
    # the list. If the specified index is invalid, raise
    # an IndexError exception.
    # TODO replace pass with your implementation
    pass

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    pass

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    pass

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    pass

if __name__ == '__main__':
    ll = Linked_List()
    cur = ll.header
    for i in range(3):
        ll.append_element(i)
    ll.insert_element_at(10,3)
    for i in range(ll.__len__()+2):
        print(cur.value)
        cur = cur.next


  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
