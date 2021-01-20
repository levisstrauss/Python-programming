
class Stack:
    def __init__(self):
        self._data = []  # Because we dont have list in python, we use array

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty")
        return self._data[-1]  # represent the last element of the list

    @property
    def data(self):
        return self._data


s = Stack()
s.push(10)
s.push(20)
print('Stack: ', s.data)
print('Length: ', len(s))
print('Is empty: ', s.is_empty())
print('Popped: ', s.pop())
print('Stack: ', s.data)