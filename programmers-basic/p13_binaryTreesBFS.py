class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def bft(self):
        queue = ArrayQueue()
        traverse = []
        if self.root:
            queue.enqueue(self.root)
        while not queue.isEmpty():
            q = queue.dequeue()
            traverse.append(q.data)
            if q.left:
                queue.enqueue(q.left)
            if q.right:
                queue.enqueue(q.right)
        return traverse


def solution(x):
    return 0
