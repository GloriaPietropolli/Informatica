"""
Implementation of the class Node and Tree (Binary tree) and of some useful function as
1) insert function
2) delete function
3) search for min/max
4) search for successor/predecessor
5) rotation to left/right
6) splay 
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
        we use the splay function (in a recursive routine) to search for a key in a tree
            :param key: value we want to find in our tree
            :return: the node where key is located
        """
        if self.key == key:
            self.splay()  # moving the node to the root
            return self
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        else:
            return None

    # def search(self, key):
    #    if key == self.key:
    #        return self
    #    elif key < self.key and self.left is not None:
    #        return self.left.search(key)
    #    elif key > self.key and self.right is not None:
    #        return self.right.search(key)
    #    else:
    #        return None

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
        """
        remove the current node
        :return: node that substitute the removed node
        """
        if self.left is None and self.right is None:  # LEAF NODE
            if self.parent is not None and self.parent.right is self:
                self.parent.right = None  # delete from the parent!!!!
            elif self.parent is not None and self.parent.left is self:
                self.parent.left = None  # delete from the parent!!!!
            # if self.parent is not None:
            #   return self.parent.splay()
            return None
        # WE JUST HAVE ONE CHILD
        child = None
        if self.left is None and self.right is not None:  # ONLY RIGHT CHILD
            child = self.right
        elif self.left is not None and self.right is None:  # ONLY LEFT CHILD
            child = self.left
        # REPLACE CHILD WITH OTHER PARENT
        if child is not None:
            child.parent = self.parent
            if self.parent is not None and self.parent.right is self:
                self.parent.right = child
            elif self.parent is not None and self.parent.left is self:
                self.parent.left = child
            # if self.parent is not None:
            #   return self.parent.splay()
            return child
        # WE HAVE BOTH CHILD
        x = self.successor()
        x.key, self.key = self.key, x.key
        x.remove()
        return self

    def str_with_offset(self, offset):
        s = "__"*offset + str(self.key) + "\n"
        if self.left is not None:
            s += self.left.str_with_offset(offset+1)
        if self.right is not None:
            s += self.right.str_with_offset(offset+1)
        return s

    # START TUTORATO 5

    def rotate_left(self):
        """
        rotation to left of a node
        :return: tree rotated to the left direction
        """
        if self.right is not None:
            a = self
            b = self.right
            a.right = b.left
            if a.right is not None:
                a.right.parent = a
            b.left = a
            if a.parent is not None:
                if a.parent.right is a:
                    a.parent.right = b
                else:
                    a.parent.left = b
            b.parent = a.parent
            a.parent = b
            return b

    def rotate_right(self):
        """
        rotation to left of a node
        :return: tree rotated to the left direction
        """
        if self.left is not None:
            a = self
            b = self.left
            a.left = b.right
            if a.left is not None:
                a.left.parent = a
            b.right = a
            if a.parent is not None:
                if a.parent.right is a:
                    a.parent.right = b
                else:
                    a.parent.left = b
            b.parent = a.parent
            a.parent = b
            return b

    def splay(self):
        p = self.parent  # parent
        if p is None:  # siamo già nella radice
            return
        g = p.parent  # grandparent
        if g is None:  # The tree is rotated on the edge between self and p
            # ZIG (only when x has odd depth at the beginning of the operation)
            if p.right is self:
                p.rotate_left()
            else:
                p.rotate_right()
            return
        # ZIG ZIG
        if p.left is self and g.left is p:
            g.rotate_right()
            p.rotate_right()
        elif p.right is self and g.right is p:
            g.rotate_left()
            p.rotate_left()
        # ZIG ZAG
        elif p.right is self and g.left is p:
            p.rotate_left()
            g.rotate_right()
        elif p.left is self and g.right is p:
            p.rotate_right()
            g.rotate_left()
        self.splay()

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
