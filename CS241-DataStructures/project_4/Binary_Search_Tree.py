class Binary_Search_Tree:

    class __BST_Node:

        def __init__(self, value):
            self.value = value
            self.height = 1
            self.left = None
            self.right = None

    def __init__(self):
        self.__root = None
        self.__size = 0 #To create array for string

    def insert_element(self, value):
        self.__root = self.__r_insert(value,self.__root)
        self.__size += 1

    def __r_insert(self, value, walker):
        if walker == None:
            return Binary_Search_Tree.__BST_Node(value)
        elif walker.value == value:
            raise ValueError
        elif walker.value > value: #Walking to the left
            walker.left = self.__r_insert(value, walker.left)
        elif walker.value < value: #Walking to the right
            walker.right = self.__r_insert(value, walker.right)

        #Updating height after each activation record
        left_height = 0
        right_height = 0
        if walker.left != None:
            left_height = walker.left.height
        if walker.right != None:
            right_height = walker.right.height
        if left_height > right_height:
            walker.height = left_height + 1
        if left_height < right_height:
            walker.height = right_height + 1
        if left_height == right_height:
            walker.height = left_height + 1
        return walker

    def remove_element(self, value):
        self.__root = self.__r_remove(value,self.__root)
        self.__size -= 1

    def __r_remove(self, value, walker):
        if walker != None:
            #Removing the value
            if walker.value == value:

                #Removal if the node has no children
                if walker.right == None and walker.left == None:
                    return None

                #Removal if the node has two children
                elif walker.right != None and walker.left != None:
                    current = walker
                    walker = walker.right
                    #Walk to smallest value in right subtree
                    while walker.left != None:
                        walker = walker.left
                    current.value = walker.value
                    current.right = self.__r_remove(walker.value,current.right)
                    return current

                #Removal if the node has one child
                elif walker.right != None or walker.left != None:
                    if walker.right != None:
                        return walker.right
                    if walker.left != None:
                        return walker.left

            elif walker.value > value:
                walker.left = self.__r_remove(value,walker.left)
            elif walker.value < value:
                walker.right = self.__r_remove(value,walker.right)

            #Updating the height after each activation record
            if walker.left == None and walker.right == None:
                walker.height = 1
            else:
                left_height = 0
                right_height = 0
                if walker.left != None:
                    left_height = walker.left.height
                if walker.right != None:
                    right_height = walker.right.height
                if left_height > right_height:
                    walker.height = left_height + 1
                if left_height < right_height:
                    walker.height = right_height + 1
                if left_height == right_height:
                    walker.height = left_height + 1
            return walker
        elif walker == None:
            raise ValueError

    def in_order(self):
        #If there's no root and the tree is empty
        if self.__root == None:
            return '[ ]'
        else:
            self.tracker = 1
            self.__string = [None] * (self.__size*2+1)
            self.__string[0] = '[ '
            self.__in_order_traversal(self.__root)
            self.__string[self.__size*2] = ' ]'
            #Joining the array for efficiency
            return ''.join(self.__string)

    def pre_order(self):
        if self.__root == None:
            return '[ ]'
        else:
            self.tracker = 1
            self.__string = [None] * (self.__size*2+1)
            self.__string[0] = '[ '
            self.__pre_order_traversal(self.__root)
            self.__string[self.__size*2] = ' ]'
            return ''.join(self.__string)

    def post_order(self):
        if self.__root == None:
            return '[ ]'
        else:
            self.tracker = 1
            self.__string = [None] * (self.__size*2+1)
            self.__string[0] = '[ '
            self.__post_order_traversal(self.__root)
            self.__string[self.__size*2] = ' ]'
            return ''.join(self.__string)


    def __in_order_traversal(self,node):
        if node == None:
            return
        else:
            self.__in_order_traversal(node.left)
            self.__string[self.tracker] = str(node.value)
            self.__string[self.tracker + 1] = ', '
            self.tracker += 2
            self.__in_order_traversal(node.right)

    def __pre_order_traversal(self,node):
        if node == None:
            return
        else:
            self.__string[self.tracker] = str(node.value)
            self.__string[self.tracker + 1] = ', '
            self.tracker += 2
            self.__pre_order_traversal(node.left)
            self.__pre_order_traversal(node.right)

    def __post_order_traversal(self,node):
        if node == None:
            return
        else:
            self.__post_order_traversal(node.left)
            self.__post_order_traversal(node.right)
            self.__string[self.tracker] = str(node.value)
            self.__string[self.tracker + 1] = ', '
            self.tracker += 2


    def get_height(self):
        if self.__root == None:
            return 0
        return self.__root.height

    def __str__(self):
        return self.in_order()

# if __name__ == '__main__':
#     pass
