# class Testing:
#
#     def __init__(self):
#     def Test(self):
#         if self == None:
#             return "Yes correct"
#         else:
#             return "No, incorrect"
#
# t = Testing()
# print(t.Test())
# a = ['1','2','3']
# b = []
# b = b.join(a)
# print(a)
#
# #In-order
# self.__traversal(node.left)
# self.__string += (str(node.value)) + ', '
# self.__traversal(node.right)
#
# #Post-order
# self.__traversal(node.left)
# self.__traversal(node.right)
# self.__string += (str(node.value)) + ', '
#
# #Pre-order
# self.__string += (str(node.value)) + ', '
# self.__traversal(node.left)
# self.__traversal(node.right)
#
#
#     def __traversal(self,node,order):
#         if node == None:
#             return
#         else:
#             if order == 2:
#                 self.__string[self.tracker] = str(node.value)
#                 self.tracker += 1
#             self.__traversal(node.left,order)
#             if order == 0:
#                 self.__string[self.tracker] = str(node.value)
#                 self.tracker += 1
#             self.__traversal(node.right,order)
#             if order == 1:
#                 self.__string[self.tracker] = str(node.value)
#                 self.tracker += 1
#         print(self.__string)
#         self.__string = ', '.join(self.__string)
#         return '[ ' + self.__string + ' ]'

# a = 10
# def checker(x):
#     if x/5 == 2:
#         print("One")
#     if x/2 == 5:
#         print("Two")
#     if x/10 == 1:
#         print("Three")
# checker(a)

#join

# a = ['[ ','a']
# def join(string):
#     return string[:len(string)]
# # print(a[0])
#
# print(ord(" "))
