class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        # This is a representation method and it will always return the representation of the object
        # we pass in
        return "Node object: data={} ".format(self.data)

    # The get method for getting the node
    def get_data(self):
        """Return the self data attribute"""
        return self.data

    def set_data(self, new_data):
        self.data = new_data  # Replace the self.data attribute with new data

    def get_next(self):  # Return the self.next attribute
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_previous(self):
        """Return the self data attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Return the self data attribute"""
        self.previous = new_previous


class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "DLL object: head={}".format(self.head)

    def is_empty(self):
        return self.head is None  # Return true if the Linkedlist is empty

    def add_front(self, new_data):
        temp = Node(new_data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)
        self.head = temp

    def size(self):  # O(n)
        size = 0
        if self.head is None:
            return 0
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def search(self, data):
        if self.head is None:
            return "The Linked list is empty. No Nodes to search."
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, data):
        if self.head is None: # Remove the current occurence of the node that content the data
            return "The Linked list is empty> No node to remove."
        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A node with that value is not present."
                else:
                    current = current.get_next()
        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())


dll = DLL()
dll.add_front("bird")
dll.add_front("apple")
dll.add_front("carrot")
print(dll.size())
dll.remove("apple")
print(dll.size())
print(dll.remove("Bird"))
