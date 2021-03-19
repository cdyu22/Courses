class Binary_Search_Tree:

    class __BST_Node:

        def __init__(self, value):
            self.value = value
            self.height = 1
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.__size = 0

    def insert_element(self, value):
        self.root = self.__r_insert(value,self.root)
        self.__size += 1

    def __r_insert(self, value, walker):

        if walker == None: #Base Case, tree found insertion point.
            return Binary_Search_Tree.__BST_Node(value)

        if walker.value == value: #Raise error if value in tree
            raise ValueError

        #Walking to the left or right
        elif walker.value > value:
            walker.left = self.__r_insert(value, walker.left)
        elif walker.value < value:
            walker.right = self.__r_insert(value, walker.right)

        #Returning balanced nodes on the walk back up
        return self.__balance(walker)


    def remove_element(self, value):
        self.root = self.__r_remove(value,self.root)
        self.__size -= 1

    def __r_remove(self, value, walker):
        if walker == None: #Raise error if value isn't in tree.
            raise ValueError

        #When we find the value to remove.
        if walker.value == value:

            #No Children
            if walker.right == None and walker.left == None:
                return None

            #Two children
            elif walker.right != None and walker.left != None:
                current = walker
                walker = walker.right
                while walker.left != None:
                    walker = walker.left
                #Replace with smallest value in right subtree
                current.value = walker.value
                #Remove the value in right subtree
                current.right = self.__r_remove(walker.value,current.right)
                return self.__height_calc(current)

            #One child
            elif walker.right != None or walker.left != None:
                if walker.right != None:
                    return self.__height_calc(walker.right)
                if walker.left != None:
                    return self.__height_calc(walker.left)

        #Recursive cases
        elif walker.value > value:
            walker.left = self.__r_remove(value,walker.left)
        elif walker.value < value:
            walker.right = self.__r_remove(value,walker.right)
        if walker.left == None and walker.right == None:
            walker.height = 1
        return self.__balance(walker)


    def __balance(self, node):
        self.__height_calc(node)
        self.__balance_checker(node)
        #If balanced, we return
        if self.balance == 0 or self.balance == -1 or self.balance == 1:
            return node

        elif self.balance == -2: #Left heavy
            l_child = node.left
            self.__balance_checker(l_child)
            if self.balance == 1: #Double rotation if necessary
                cur = l_child.right.left
                l_child.right.left = l_child
                node.left = l_child.right
                l_child.right = cur
                l_child = node.left
                self.__height_calc(l_child)
                self.__height_calc(l_child.left)
            cur = l_child.right #General rotation
            l_child.right = node
            node.left = cur
            self.__height_calc(node)
            self.__height_calc(l_child)
            return l_child

        elif self.balance == 2: #Right heavy
            r_child = node.right
            self.__balance_checker(r_child)
            if self.balance == -1: #Double rotation if necessary
                cur = r_child.left.right
                r_child.left.right = r_child
                node.right = r_child.left
                r_child.left = cur
                r_child = node.right
                self.__height_calc(r_child)
                self.__height_calc(r_child.right)
            cur = r_child.left #General rotation
            r_child.left = node
            node.right = cur
            self.__height_calc(node)
            self.__height_calc(r_child)
            return r_child

    def __height_calc(self, node):
        left_height = 0
        right_height = 0
        #Checking if they exist
        if node.left != None:
            left_height = node.left.height
        if node.right != None:
            right_height = node.right.height
        #Updating height
        if left_height > right_height:
            node.height = left_height + 1
        if left_height < right_height:
            node.height = right_height + 1
        if left_height == right_height:
            node.height = left_height + 1
        return node

    def __balance_checker(self,node):
        self.balance = 0
        left_height = 0
        right_height = 0
        #Checking if they exist
        if node.left != None:
            left_height = node.left.height
        if node.right != None:
            right_height = node.right.height
        self.balance = right_height - left_height

    def in_order(self):
        #If there's no root and the tree is empty.
        if self.root == None:
            return '[ ]'
        else:
            self.tracker = 1
            self.__string = [None] * (self.__size*2+1)
            self.__string[0] = '[ '
            self.__in_order_traversal(self.root)
            self.__string[self.__size*2] = ' ]'
            #Joining the array for efficiency.
            return ''.join(self.__string)

    def pre_order(self):
        if self.root == None:
            return '[ ]'
        else:
            self.tracker = 1
            self.__string = [None] * (self.__size*2+1)
            self.__string[0] = '[ '
            self.__pre_order_traversal(self.root)
            self.__string[self.__size*2] = ' ]'
            return ''.join(self.__string)

    def post_order(self):
        if self.root == None:
            return '[ ]'
        else:
            self.tracker = 1
            self.__string = [None] * (self.__size*2+1)
            self.__string[0] = '[ '
            self.__post_order_traversal(self.root)
            self.__string[self.__size*2] = ' ]'
            return ''.join(self.__string)

    def to_list(self):
        self.tracker = 0 #Set to zero as no '[ ' in cell zero.
        self.__list = [None] * (self.__size)
        self.__to_list_traversal(self.root)
        return self.__list

    def __in_order_traversal(self,node):
        if node == None: #Base case
            return
        else: #Recursive Cases
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

    def __to_list_traversal(self,node):
        if node == None: #Will also return if no root.
            return
        else:
            self.__to_list_traversal(node.left)
            self.__list[self.tracker] = node.value
            self.tracker += 1
            self.__to_list_traversal(node.right)

    def get_height(self):
        if self.root == None:
            return 0
        return self.root.height

    def __str__(self):
        return self.in_order()

# if __name__ == '__main__':
#     pass
