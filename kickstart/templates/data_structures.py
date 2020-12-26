import heapq

def example_heap_usage():
    l = [6, 2, 4, 3]
    print(l)
    heapq.heapify(l)  # turns list into heap inplace
    print(l)
    heapq.heappush(l, 7)  # add new item, log(n)
    heapq.heappush(l, 5)  # add new item, log(n)
    heapq.heappush(l, 1)  # add new item, log(n)

    print(l) # does not print correct order
    print(l[0]) # print min
    while len(l) !=0:
        first = heapq.heappop(l)  # remove min and return it
        print(first) # pop gives correct element
    # if you want a max heap then use negative numbers


from collections import deque
def example_usage_double_end_queue():
    a = deque([6,7,8])
    a.append(2)
    a.appendleft(3)
    print(a)
    a.pop()
    a.popleft()
    a = deque([6,7,8],maxlen=3)
    a.append(2)
    print(a)
    a.appendleft(3)
    print(a)


class BinaryTree:
    # some first idea of binary tree implementation
    # need to tune and add complicated balancing and deletion
    def __init__(self, node=None):
        self.root = node

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        search_node = self.root
        while search_node is not None:
            if value <= search_node.value:
                if search_node.left is None:
                    search_node.left = node
                    return
                search_node = search_node.left
            else:
                if search_node.right is None:
                    search_node.right = node
                    return
                search_node = search_node.right

    def max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    def print_tree(self):
        # hacky
        print("tree start")
        if self.root is None:
            print("Empty tree")
            return
        nodes = [self.root]
        while len(nodes) > 0:
            print([x.value for x in nodes])
            new_nodes = []
            for n in nodes:
                if n.left is not None:
                    new_nodes.append(n.left)
                if n.right is not None:
                    new_nodes.append(n.right)
            nodes = new_nodes

    def remove_max(self):
        if self.root is None:
            return
        if self.root.right is None:
            if self.root.left is None:
                self.root = None
            else:
                self.root = self.root.left
            return
        parent = self.root
        node = self.root.right
        while node.right is not None:
            parent = node
            node = node.right
        parent.right = node.left


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
