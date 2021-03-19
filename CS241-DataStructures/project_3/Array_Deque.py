from Deque import Deque

class Array_Deque(Deque):
    def __init__(self):
        self.__capacity = 1
        self.__contents = [None] * self.__capacity
        self.__size = 0
        self.__start = 0
        self.__end = 0

    def __str__(self):
        if len(self) == 0:
            return '[ ]'
        string = [None] * len(self)
        for i in range(len(self)):
            #Need to start from self.__start and wrap around if necessary.
            string[i] = str(self.__contents[(i+self.__start)%self.__capacity])
        string = ', '.join(string)
        return '[ ' + string + ' ]'

    def __len__(self):
        return self.__size

    def __grow(self):
        self.__holder = [None] * self.__capacity * 2
        for i in range(len(self.__contents)):
            #Copy all the values in self.__contents into an array twice as big.
            self.__holder[i] = self.__contents[(self.__start+i)%self.__capacity]
        self.__contents = self.__holder #Point contents to new list.
        self.__capacity *= 2
        self.__start = 0
        self.__end = len(self) - 1

    def push_front(self, val):
        if len(self) == self.__capacity:
            self.__grow()
        if self.__start > 0:
            self.__start -= 1
        elif self.__start == 0: #If we need to wrap around the array.
            self.__start = self.__capacity - 1
        self.__contents[self.__start] = val
        self.__size += 1

    def pop_front(self):
        if len(self) == 0:
            return
        value = self.__contents[self.__start]
        if self.__start == self.__capacity - 1: #To wrap around if needed.
            self.__start = 0
        else:
            self.__start += 1
        self.__size -= 1
        return value

    def peek_front(self):
        if len(self) == 0:
        #Need to do this, as there could be a value we didn't write over.
            return
        return self.__contents[self.__start]

    def push_back(self, val):
        if len(self) == self.__capacity:
            self.__grow()
        if self.__end < self.__capacity - 1: #To wrap around if needed
            self.__end += 1
        elif self.__end == self.__capacity - 1:
            self.__end = 0
        self.__contents[self.__end] = val
        self.__size += 1

    def pop_back(self):
        if len(self) == 0:
            return
        value = self.__contents[self.__end]
        if self.__end == 0:
            self.__end = self.__capacity - 1 #Wrap around if needed.
        else:
            self.__end -= 1
        self.__size -= 1
        return value

    def peek_back(self):
        if len(self) == 0:
            return
        return self.__contents[self.__end]

# if __name__ == '__main__':
#     pass
