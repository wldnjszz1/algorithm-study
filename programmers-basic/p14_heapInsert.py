class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        while i > 1:
            if self.data[i] > self.data[i//2]:
                self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
                i = i // 2
            else:
                break


def solution(x):
    return 0