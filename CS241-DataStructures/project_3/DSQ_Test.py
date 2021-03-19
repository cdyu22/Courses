import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):

    def setUp(self):
        self.__deque = get_deque()
        self.__stack = Stack()
        self.__queue = Queue()

    def test_empty_deque(self):
        self.assertEqual('[ ]', str(self.__deque))

    def test__str__one(self):
        self.__deque.push_front('Victory')
        self.assertEqual('[ Victory ]', str(self.__deque))

    def test_len_empty_list(self):
        self.assertEqual(0,len(self.__deque))

    def test_len_one_value(self):
        self.__deque.push_front(0)
        self.assertEqual(1, len(self.__deque))

    def test_len_two_values(self):
        self.__deque.push_front(0)
        self.__deque.push_back(1)
        self.assertEqual(2, len(self.__deque))

    def test__str__two(self):
        self.__deque.push_front('Data')
        self.__deque.push_back('Structures')
        self.assertEqual('[ Data, Structures ]', str(self.__deque))

    def test_push_front_empty(self):
        self.__deque.push_front(0)
        self.assertEqual('[ 0 ]', str(self.__deque))

    def test_push_back_empty(self):
        self.__deque.push_back(0)
        self.assertEqual('[ 0 ]', str(self.__deque))

    def test_push_front_twice(self):
        self.__deque.push_front(0)
        self.__deque.push_front(1)
        self.assertEqual('[ 1, 0 ]', str(self.__deque))

    def test_push_back_twice(self):
        self.__deque.push_back(0)
        self.__deque.push_back(1)
        self.assertEqual('[ 0, 1 ]', str(self.__deque))

    def test_push_front_then_back(self):
        self.__deque.push_front(0)
        self.__deque.push_back(1)
        self.assertEqual('[ 0, 1 ]', str(self.__deque))

    def test_push_back_then_front(self):
        self.__deque.push_back(1)
        self.__deque.push_front(0)
        self.assertEqual('[ 0, 1 ]', str(self.__deque))

    def test_pop_front_empty(self):
        self.assertEqual(None, self.__deque.pop_front())

    def test_pop_front(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.pop_front()
        self.assertEqual('[ 2, 3 ]', str(self.__deque))

    def test_pop_front_return_value(self):
        self.__deque.push_front(0)
        self.assertEqual(0, self.__deque.pop_front())

    def test_pop_back_empty(self):
        self.assertEqual(None, self.__deque.pop_back())

    def test_pop_back(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.push_back(3)
        self.__deque.pop_back()
        self.assertEqual('[ 1, 2 ]', str(self.__deque))

    def test_pop_back_return_value(self):
        self.__deque.push_front(0)
        self.assertEqual(0, self.__deque.pop_back())

    def test_push_front_pop_back(self):
        self.__deque.push_front(2)
        self.__deque.push_front(1)
        self.__deque.push_front(0)
        self.__deque.pop_back()
        self.assertEqual('[ 0, 1 ]', str(self.__deque))

    def test_push_back_pop_front(self):
        self.__deque.push_back(0)
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.__deque.pop_front()
        self.assertEqual('[ 1, 2 ]', str(self.__deque))

    def test_peek_front(self):
        self.__deque.push_back(0)
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(0,self.__deque.peek_front())

    def test_peek_front_empty(self):
        self.assertEqual(None, self.__deque.peek_front())

    def test_peek_front_length_impact(self):
        self.__deque.push_back(0)
        self.__deque.push_back(1)
        self.__deque.peek_front()
        self.assertEqual(2, len(self.__deque))

    def test_peek_back(self):
        self.__deque.push_back(0)
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(2,self.__deque.peek_back())

    def test_peek_back_empty(self):
        self.assertEqual(None,self.__deque.peek_back())

    def test_peek_back_length_impact(self):
        self.__deque.push_back(0)
        self.__deque.push_back(1)
        self.__deque.peek_back()
        self.assertEqual(2, len(self.__deque))

    def test_growth(self):
        for i in range(10):
            self.__deque.push_back(i+1)
        self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]', str(self.__deque))

    def test_growth_remove_one(self):
        for i in range(10):
            self.__deque.push_back(i+1)
        self.__deque.pop_front()
        self.assertEqual('[ 2, 3, 4, 5, 6, 7, 8, 9, 10 ]', str(self.__deque))

#_______________________________stack tests_____________________________________
    def test_str_empty_stack(self):
        self.assertEqual('[ ]', str(self.__stack))

    def test_len_empty_stack(self):
        self.assertEqual(0, len(self.__stack))

    def test_str_one(self):
        self.__stack.push('Victory')
        self.assertEqual('[ Victory ]', str(self.__stack))

    def test_str_two(self):
        self.__stack.push('Structures')
        self.__stack.push('Data')
        self.assertEqual('[ Data, Structures ]', str(self.__stack))

    def test_push(self):
        for i in range(5):
            self.__stack.push(i+1)
        self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__stack))

    def test_pop_one_value(self):
        self.__stack.push(1)
        self.__stack.pop()
        self.assertEqual('[ ]', str(self.__stack))

    def test_pop_two_value(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.pop()
        self.assertEqual('[ 1 ]', str(self.__stack))

    def test_pop_return_value(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.assertEqual(3, self.__stack.pop())

    def test_pop_empty_list(self):
        self.assertEqual(None, self.__stack.pop())

    def test_peek_one_value(self):
        self.__stack.push(1)
        self.assertEqual(1, self.__stack.pop())

    def test_peek_two_value(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.assertEqual(2, self.__stack.pop())

    def test_peek_length_impact(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.peek()
        self.assertEqual(3, len(self.__stack))

    def test_peek_empty_stack(self):
        self.assertEqual(None, self.__stack.peek())

#______________________________queue tests______________________________________
    def test_str_empty_queue(self):
        self.assertEqual('[ ]', str(self.__queue))

    def test_len_empty_queue(self):
        self.assertEqual(0, len(self.__queue))

    def test_queue_string_one(self):
        self.__queue.enqueue('Victory')
        self.assertEqual('[ Victory ]', str(self.__queue))

    def test_len_one(self):
        self.__queue.enqueue(1)
        self.assertEqual(1, len(self.__queue))

    def test_queue_string_two(self):
        self.__queue.enqueue('Data')
        self.__queue.enqueue('Structures')
        self.assertEqual('[ Data, Structures ]', str(self.__queue))

    def test_len_two(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.assertEqual(2, len(self.__queue))

    def test_dequeue_removes(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.dequeue()
        self.assertEqual('[ 2 ]', str(self.__queue))

    def test_len_with_dequeue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.dequeue()
        self.assertEqual(1, len(self.__queue))

    def test_dequeue_return(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.assertEqual(1, self.__queue.dequeue())

if __name__ == '__main__':
    unittest.main()
