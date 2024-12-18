'''class Heap:
    
    def __init__(self, a):
        self.array = a
        for i in range(len(self.array)//2, -1, -1):
            self.siftDown(i)
    
    def siftDown(self, i):
        while 2 * i + 1 < len(self.array):
            max_child_index = 2 * i + 1
            if 2 * i + 2 < len(self.array) and self.array[2 * i + 1] < self.array[2 * i + 2]:
                max_child_index = 2 * i + 2
            if self.array[i] > self.array[max_child_index]:
                break
            self.array[i], self.array[max_child_index] = self.array[max_child_index], self.array[i]
            i = max_child_index
        return
    
    def siftUp(self, i):
        while self.array[i] > self.array[(i - 1) // 2] and i > 0:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2
        return
    
    def add(self, value):
        self.array.append(value)
        self.siftUp(len(self.array) - 1)
    
    def pop(self):
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.siftDown(0)
        return result

n, k = list(map(int, input().split()))
h = Heap([])
for element in list(map(int, input().split())):
    # Этот цикл напишете сами
    pass
h.array.sort()
print(" ".join(map(str, h.array)))
'''



class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_value

    def _bubble_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if (left_child_index < len(self.heap) and
                self.heap[left_child_index] < self.heap[smallest]):
            smallest = left_child_index

        if (right_child_index < len(self.heap) and
                self.heap[right_child_index] < self.heap[smallest]):
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

# Пример использования
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)

print("Минимум:", min_heap.get_min())  # Минимум: 1
print("Извлечение минимума:", min_heap.extract_min())  # Извлечение минимума: 1
print("Новый минимум:", min_heap.get_min())  # Новый минимум: 3


