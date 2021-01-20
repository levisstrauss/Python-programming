from DataStructuresAndAlgorithmsLinkedin.exceptions import Empty


class DeQueue:

    def __init__(self):
        self._data = []
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def add_first(self, e):
        self._data.insert(self._front, e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        value = self._data.pop(self._front)
        return value

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        value = self._data.pop()
        return value


d = DeQueue()
d.add_last(10)
d.add_last(20)
d.add_last(30)
print(d._data)
d.delete_first()
print(d._data)
