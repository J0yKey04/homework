'''
Бинарный поиск

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    
    def __init__(self):
        self.root = None
'''


from math import log, ceil

class SegmentTree:

    def __init__(self, a):
        self.array = a
        k = 2 ** ceil(log(len(a), 2)) - len(a)
        self.array = [0] * (len(a) + k - 1) + self.array + [0] * k
        for i in range(len(a) + k - 2, -1, -1):
            self.array[i] = self.array[2 * i + 1] + self.array[2 * i + 2]
        self.size = len(a)


    def sum(self):
        return self.array(0)
    
    def add(self, value):
        self.size += 1
        if 2 ** int(log(self.size, 2)) <= self.size:
            i = self.size - 2 + 2 ** ceil(log(self.size, 2))
            self.array[i] = value
            while i >= 0:
                self.array[(i - 1 // 2)] += value
                i = (i - 1) // 2

    def remove(self, value):
        self.size += 1
        if 2 ** int(log(self.size, 2)) == self.size:




t = SegmentTree([5, 24, 61])
print(t.array)


