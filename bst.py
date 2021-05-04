"""
Implementation of the class Node and Tree (Binary tree) and of some useful function as
1) insert function
2) delete function
3) search for min/max
4) search for successor/predecessor
"""
class Node:

    def __init__(self, key, parent, left, right):
        """
        :param key: attribute of the node
        :param parent: parent of the node (i.e. the node above it)
        :param left: left child of the node
        :param right:  right child of the node
        """
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def search(self, key):
        """
        recursive function to search for a values in a tree
        :param key: value we want to find in our tree
        :return: the node where key is located
        """
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        else:
            return None

    def mimimum(self):
        """
        recursive function to find the min of the bst, i.e. the child that is in the extreme left
        :return: the min key
        """
        if self.left is None:
            return self
        else:
            return self.left.mimimum()

    def maximum(self):
        """
        recursive function to find the max of the bst, i.e. the child that is in the extreme right
        :return: the max key
        """
        if self.right is None:
            return self
        else:
            return self.right.maximum()

    def insert(self, key):
        """
        recursive function to insert in the right place the value of a child
        :param key: key we want to insert
        :return: None
        """
        if key <= self.key:
            if self.left is None:
                self.left = Node(key, self, None, None)
            else:
                self.left.insert(key)
        else:  # key > self.key
            if self.right is None:
                self.right = Node(key, self, None, None)
            else:
                self.right.insert(key)

    def successor(self):
        if self.right is not None:
            return self.right.mimimum()
        x = self
        y = x.parent
        while y is not None and y.right is x:
            y = y.parent
            x = x.parent
        return y

    def predecessor(self):
        if self.left is not None:
            return self.right.maximum()
        x = self
        y = x.parent
        while y is not None and y.left is x:
            y = y.parent
            x = x.parent
        return y

    def remove(self):
        if self.left is None and self.right is None:  # leaf
            if self.parent is not None and self.parent.right is self:
                self.parent.right = None  # delete from the parent!!!!
            elif self.parent is not None and self.parent.left is self:
                self.parent.left = None  # delete from the parent!!!!
            return None
        # we have just one child
        child = None
        if self.left is None and self.right is not None:  # only right child
            child = self.right
        elif self.left is not None and self.right is None:  # only left child
            child = self.left
        # replace child with the parent
        if child is not None:
            child.parent = self.parent
            if self.parent is not None and self.parent.right is self:
                self.parent.right = child
            elif self.parent is not None and self.parent.left is self:
                self.parent.left = child
            return child
        # we have both child
        x = self.successor()
        x.key, self.key = self.key, x.key  # scambiamo il contenuto
        x.remove()
        return self

    def str_with_offset(self, offset):
        s = "__"*offset + str(self.key) + "\n"
        if self.left is not None:
            s += self.left.str_with_offset(offset+1)
        if self.right is not None:
            s += self.right.str_with_offset(offset+1)
        return s

    def __str__(self):
        return self.str_with_offset(0)


class Tree:

    def __init__(self):
        self.root = None

    def search(self, k):
        if self.root is None:
            return None
        else:
            return self.root.search(k)

    def insert(self, k):
        if self.root is None:
            self.root = Node(k, None, None, None)
        else:
            self.root.insert(k)

    def maximum(self):
        if self.root is None:
            return None
        else:
            return self.root.maximum()

    def minimum(self):
        if self.root is None:
            return None
        else:
            return self.root.minimum()

    def successor(self, x):
        return x.successor()

    def predecessor(self, x):
        return x.predecessor()

    def remove(self, x):
        if x is self.root:
            self.root = x.remove()
        else:
            x.remove()

    def __str__(self):
        return str(self.root)


t = Tree()
t.insert(12)
t.insert(3)
t.insert(5)
t.insert(17)
t.insert(8)
t.insert(23)
t.insert(13)
t.insert(4)
t.insert(15)
t.insert(2)
print(t)