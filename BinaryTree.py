from hashlib import new
from locale import currency


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.data}"

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
            Insert(data: any) -> None:\n 
            creates a new Node from the data passed in and adds it to the tree
            If the data is already in the tree, does not insert it again
        '''
        new_node = Node(data)
        # if tree empty, make new_node the root
        if not self.root:
            self.root = new_node
        else:
            curr_node = self.root
            while curr_node:
                if new_node.data < curr_node.data:
                    if not curr_node.left:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left
                elif new_node.data > curr_node.data:
                    if not curr_node.right:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right
                else:
                    return
    def dfs(self, val):
        '''
            dfs(val: any) -> value or bool:\n 
            Performs depth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        if not self.root:
            return False
        else:
            curr_node = self.root
            while curr_node:
                if val < curr_node.data:
                    curr_node = curr_node.left
                elif val > curr_node.data:
                    curr_node = curr_node.right
                else:
                    return curr_node
            return False
    def bfs(self, val):
        '''
            bfs(val: any) -> value or bool:\n
            Performs breadth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        if not self.root:
            return False
        else:
            # queue to keep track of each level
            queue = [self.root]
            while len(queue) > 0:
                # examine (and dequeue) node at start of queue
                curr_node = queue.pop(0)
                # if it contains "val", return node
                if curr_node.data == val:
                    return curr_node
                # take children of the node we dequeued and enqueue them (only if they are not None)
                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)
            return False
    # print out all the nodes
    def print(self, node=None):
        '''
            print() -> None:\n
            prints out all values recursively (in a depth first search fashion)
            default start is at root node
        '''
        # if this is the first invocation
        if not node:
            node = self.root
        print(node)    # depth-first-search
        if node.left:
            self.print(node.left)
        # print(node)    # in-order-traversal
        if node.right:
            self.print(node.right)

    def size(self):
        '''
            size() -> int:\n 
            Calculate the number of nodes in the tree, starting from the root
        '''
        pass
    def height(self):
        '''
            height() -> int:\n 
            Calculate the maximum depth of nodes starting at the root
        '''
        pass
    def get_max(self):
        '''
            get_max() -> int:\n 
            perform depth first search
            Calculate the maximum value held in the tree
        '''
        if not self.root:
            return False
        else:
            curr_node = self.root
            while curr_node.right:
                curr_node = curr_node.right
            return curr_node
    def get_min(self):
        '''
            get_min() -> int:\n 
            perform depth first search
            Calculate the minimum value held in the tree
        '''
        if not self.root:
            return False
        else:
            curr_node = self.root
            while curr_node.left:
                curr_node = curr_node.left
            return curr_node

my_tree = BinaryTree()
my_tree.insert(15)
my_tree.insert(10)
my_tree.insert(16)
print(f"{my_tree.root.left} <- {my_tree.root} -> {my_tree.root.right}")
my_tree.insert(19)
my_tree.insert(22)
my_tree.insert(17)
my_tree.insert(6)
my_tree.insert(9)
my_tree.insert(2)
# my_tree.print()
print(my_tree.dfs(2))
print(my_tree.dfs(4))
print(my_tree.bfs(6))
print(my_tree.bfs(8))

print(my_tree.get_max())
print(my_tree.get_min())
