class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        else:
            if pos == 1:
                if self.nodeCount == 1:
                    delete = self.head
                    self.head = None
                    self.tail = None
                else:
                    delete = self.head
                    self.head = self.head.next
                self.nodeCount -= 1
                return delete.data
            else:
                if pos == self.nodeCount:
                    delete = self.tail
                    self.tail = self.getAt(pos - 1)
                    self.tail.next = None
                else:
                    delete = self.getAt(pos)
                    prev = self.getAt(pos - 1)
                    prev.next = delete.next

                self.nodeCount -= 1
                return delete.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

# 정확성:100, 효울성:100