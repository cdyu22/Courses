class Min_Heap:

    class Huffman_Tree:
        def __init__(self,tree,value):
            self.tree = key
            self.value = value
            self.left = None
            self.right = None

        def get_key(self):
            return self.tree

        def get_value(self):
            return self.value

        def __str__(self):
            return str(key) + str(value)

    def __init__(self,length):
        self.heap = [None]*length

    def insert(self,tree,value):
        insert = 0
        newest = self.Huffman_Tree(tree,value)
        while self.heap[insert] == None:
            pass

    def remove(self):
        pass

    def __str__(self):
        return ''.join(self.heap)

string = input("What's the string? ")
string = string.lower()
print(string)
print(type(string))

string = list(string)
freq = {}

for item in string:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# for key, value in freq.items():
#     print(key, value)

alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for item in alphabet:
    if item in freq:
        print(item,freq[item])
print(len(string))
