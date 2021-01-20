from _queue import Empty


class Queue:

    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        self._data.append(e)
        self._size = self._size + 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._front = self._front + 1
        self._size = self._size - 1
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    @property
    def data(self):
        return self._data


s = Queue()
s.enqueue(10)
s.enqueue(20)

print('Queue: ', s.data)
print('Length: ', len(s))
print('Dequeue: ', s.dequeue())
print('Queue: ', s.data)




